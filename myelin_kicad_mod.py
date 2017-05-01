# This file generates KiCad footprint (.kicad_mod) files directly from
# a Python script, that specifies all pins, pads, and artwork.

INCH = 25.4
ALL_CU = "*.Cu" # for pins that go all the way through
FRONT_CU = "F.Cu"
BACK_CU = "B.Cu"
FRONT_SILK = "F.SilkS"
BACK_SILK = "B.SilkS"
FRONT_PASTE = "F.Paste"
BACK_PASTE = "B.Paste"
ALL_MASK = "*.Mask" # for pins that go all the way through
FRONT_MASK = "F.Mask"
BACK_MASK = "B.Mask"
EDGE_CUTS = "Edge.Cuts"
# standard layer sets for pins and pads
FRONT_PIN = [ALL_CU, ALL_MASK, FRONT_SILK]
FRONT_PAD = [FRONT_CU, FRONT_MASK, FRONT_PASTE]
FRONT_TEXT = [FRONT_SILK]
BACK_TEXT = [BACK_SILK]
BACK_PAD = [BACK_CU, BACK_MASK, BACK_PASTE]
EDGE = [EDGE_CUTS]

# format python list into kicad netlist format
def dump_list(list):
    children = [
        dump_list(item) if type(item) == type([]) else fmt_item(item)
        for item in list]
    children_joined = " ".join(children)
    if len(children_joined) > 200:
        children_joined = "\n".join(children)
    r = "(%s)" % children_joined.strip()
    #print "***\n%s\n->%s\n***" % (`list`, r)
    return r

# format list entry for dump_list()
def fmt_item(item):
    if type(item) == type(""):
        if len(item) == 0 or item.find(" ") != -1:
            return '"%s"' % item.replace('"', "'") # munge
    return str(item)

class Element:
    pass

class Text(Element):
    def __init__(self, x, y, text, kind='user', layers=None, rotation=0, mirror=False, bottom=False, hide=False):
        if layers is None: layers = FRONT_TEXT
        if bottom:
            # shortcut to get text on the bottom layer
            mirror=True
            layers=BACK_TEXT
        self.x, self.y, self.text, self.kind, self.layers, self.rotation, self.mirror, self.hide = (
            x, y, text, kind, layers[:], rotation, mirror, hide)
    def as_list(self):
        effects = ["effects", ["font", ["size", 1, 1], ["thickness", 0.15]]]
        if self.mirror:
            effects.append(["justify", "mirror"])
        fp_text = ["fp_text", self.kind, self.text, ["at", self.x, self.y, self.rotation], ["layer"] + self.layers]
        if self.hide: fp_text.append("hide")
        fp_text.append(effects)
        return fp_text

class Line(Element):
    def __init__(self, x0, y0, x1, y1, layers=None):
        if layers is None: layers = [FRONT_SILK]
        self.x0, self.y0, self.x1, self.y1, self.layers = x0, y0, x1, y1, layers[:]
    def as_list(self):
        return ["fp_line", ["start", self.x0, self.y0], ["end", self.x1, self.y1], ["layer"] + self.layers, ["width", "0.15"]]

class Circle(Element):
    def __init__(self, x0, y0, r, layers=None):
        if layers is None: layers = [FRONT_SILK]
        self.x0, self.y0, self.r, self.layers = x0, y0, r, layers[:]
    def as_list(self):
        return ["fp_circle", ["center", self.x0, self.y0], ["end", self.x0, self.y0 + self.r], ["layer"] + self.layers, ["width", "0.15"]]

class Pin(Element):
    def __init__(self, name, x, y, dia, hole_dia, layers=None, square=False, solid_connect=False):
        if layers is None: layers = FRONT_PIN
        self.name, self.x, self.y, self.dia, self.hole_dia, self.layers, self.square, self.solid_connect = (
            name, x, y, dia, hole_dia, layers[:], square, solid_connect)
    def as_list(self):
        r = [
            "pad", self.name, "thru_hole",
            "rect" if self.square else "circle",
            ["at", self.x, self.y],
            ["size", self.dia, self.dia],
            ["drill", self.hole_dia],
            ["layers"] + self.layers,
        ]
        if self.solid_connect:
            r.append(["zone_connect", 2])
        return r

class Hole(Pin):
    def __init__(self, x, y, hole_dia):
        self.x, self.y, self.hole_dia, self.layers = x, y, hole_dia, [ALL_CU]
    def as_list(self):
        return ["pad", "", "np_thru_hole", "circle", ["at", self.x, self.y], ["size", self.hole_dia, self.hole_dia], ["drill", self.hole_dia], ["layers"] + self.layers]

class Pad(Element):
    def __init__(self, name, x, y, w, h, layers=None):
        if layers is None: layers = FRONT_PAD
        self.name, self.x, self.y, self.w, self.h, self.layers = name, x, y, w, h, layers[:]
    def rotate(self, degrees):
        # rotate counterclockwise around the origin in increments of 90 degrees
        for r in range(int(degrees / 90.0)):
            self.x, self.y = -self.y, self.x
            self.w, self.h = self.h, self.w
        return self # allow chaining
    def as_list(self):
        return ["pad", self.name, "smd", "rect", ["at", self.x, self.y], ["size", self.w, self.h], ["layers"] + self.layers]

class Module:
    def __init__(self, identifier, description, ref_x=0, ref_y=-1, value_x=0, value_y=1, silkscreen=True):
        self.identifier = identifier
        self.description = description
        self.ref_text = Text(ref_x, ref_y, "REF**", "reference", hide=not silkscreen)
        self.value_text = Text(value_x, value_y, self.identifier, "value", hide=not silkscreen)
        self.elements = [self.ref_text, self.value_text]

    def add(self, element):
        self.elements.append(element)

    def save(self):
        fn = "%s.kicad_mod" % self.identifier
        data = dump_list(self.as_list())
        print>>open(fn, "w"), data
        print "Written to %s:\n\n%s" % (fn, data)

    def as_list(self):
        return [
            "module", self.identifier,
            ["descr", self.description],
        ] + [element.as_list() for element in self.elements]
