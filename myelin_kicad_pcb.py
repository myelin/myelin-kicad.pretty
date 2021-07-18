from __future__ import print_function

# This file generates KiCad netlist (.net) files directly from a
# Python script, that specifies all parts, connections, and
# footprints.

import csv
import os
import re
import types

class PCB:
    def __init__(self):
        self.nets = {}
        self.components = {}

    @classmethod
    def reset(cls):
        cls.pcb = cls()

reset = PCB.reset

reset()

def pcb():
    return PCB.pcb

# format list entry for dump_list()
def fmt_item(item):
    if type(item) == type(""):
        if not len(item) or item.find(" ") != -1:
            return '"%s"' % item.replace('"', "'") # munge
    return str(item)

# format python list into kicad netlist format
def dump_list(list):
    # Rules for nice display:
    # If a list contains only strings, render it in one line
    # If a list can be rendered in one line, render it in one line
    # Otherwise render it as a block

    rendered_items = [
        dump_list(item) if type(item) == type([]) else fmt_item(item)
        for item in list]

    # Just a single value?
    if len(rendered_items) < 2:
        return "(%s)" % rendered_items[0]

    # Will it fit in a line?
    total_length = 2 + len(rendered_items) + sum(len(item) for item in rendered_items)
    single_line = "(%s)" % " ".join(rendered_items)
    if len(single_line) < 120 and "\n" not in single_line:
        return single_line

    # Special case for the root, so we pass the regex used to detect file format
    if rendered_items[0] == "export":
        return "(%s %s)" % (
            rendered_items[0],
            "\n  ".join(item.replace("\n", "\n  ") for item in rendered_items[1:]),
        )

    # Render as a block
    return "(%s)" % "\n  ".join(item.replace("\n", "\n  ") for item in rendered_items)

# write netlist to disk
def dump_netlist(fn):
    export_components = []
    export_nets = []

    for identifier, component in sorted(pcb().components.items()):
        export_components.append([
            "comp", ["ref", component.identifier],
            ["value", component.value],
            ["footprint", component.footprint],
        ])

    # verify consistent casing in netlist names: <lower case version> => {netname, netname, ...}
    net_case_check = {}

    # verify everything gets connected
    nets_with_one_node = set()

    net_counter = 0
    for net_id, pins in sorted(pcb().nets.items()):
        net_case_check.setdefault(net_id.lower(), set()).add(net_id)
        net_counter += 1
        print("=== %s ===" % net_id)
        export_nodes = []
        for pin in pins:
            print("  - %s.%s (%s %s)" % (pin.component.identifier, pin.number, pin.component.value, pin.name))
            export_nodes.append(["node", ["ref", pin.component.identifier], ["pin", pin.number]])
        export_nets.append(["net", ["code", net_counter], ["name", net_id if net_id else "_default"]] + export_nodes)
        if len(export_nodes) == 1:
            nets_with_one_node.add(net_id)

    for net_id in nets_with_one_node:
        print("WARNING: net %s only has one attached node" % net_id)

    bad_nets_exist = 0
    for net_ids in net_case_check.values():
        if len(net_ids) == 1:
            continue
        print("Inconsistent casing in nets: %s" % " ".join(net_ids))
        bad_nets_exist = 1
    if bad_nets_exist:
        raise Exception("Inconsistent net casing; see details above")

    print(dump_list([
        "export",
        ["version", "D"],
        ["components"] + export_components,
        ["nets"] + export_nets,
    ]), file=open(fn, "w"))
    print("Saved netlist to %s" % fn)

def dump_bom(fn, readable_fn, seeed_fn=None, jlc_fn=None):
    # Write readable BOM and collate items
    list = [["Identifier", "Value", "Description", "KiCad package", "LCSC part"]]
    merged = {}  # map of (part number, link) -> [identifier, identifier, ...]
    jlc_merged = {}  # map of (LCSC ID, comment, footprint) -> [identifier, ...]
    rf = open(readable_fn, "w")
    print("""This is the human-readable bill of materials.
See %s for a terser version suitable for spreadsheet import.
""" % fn, file=rf)
    for identifier, component in sorted(
        pcb().components.items(),
        key=lambda i: (i[1].desc, i[1].value, i[0])
    ):
        if component.exclude_from_bom: continue
        if component.footprint == "myelin-kicad:via_single":
            continue
        item = [identifier, component.value, component.desc, component.footprint, component.jlc_part or ""]
        list.append(item)

        if not component.partno or not component.link:
            print("WARNING: component %s is missing partno or link" % component.identifier)
        else:
            mergekey = (component.partno, component.link)
            merged.setdefault(mergekey, []).append(component.identifier)

        if component.jlc_part:
            mergekey = (component.jlc_part, component.desc, component.footprint)
            jlc_merged.setdefault(mergekey, []).append(component.identifier)
        print("%s\n- Value: %s\n- Description: %s\n- KiCad package: %s\n" % tuple(item)[:4], file=rf)

    # Write simple spreadsheet BOM
    f = open(fn, "w")
    for line in list:
        print("\t".join(line), file=f)
    print("Saved BOM to %s" % fn)

    # Write Seeed-format BOM; see https://www.seeedstudio.com/fusion_pcb.html
    if seeed_fn:
        assert seeed_fn.endswith(".csv"), "Seeed Fusion BOM files must be in CSV/XLS/XLSX format"
        list = [["Comment", "Designator", "Footprint", "LCSC"]]
        for (partno, link), identifiers in merged.items():
            print(partno, link, identifiers)
        print("Saved Seeed-format BOM to %s" % seeed_fn)

    # Write JLC-format BOM; see https://support.jlcpcb.com/article/84-how-to-generate-the-bom-and-centroid-file-from-kicad
    if jlc_fn:
        assert jlc_fn.endswith(".csv"), "JLC PCBA BOM files must be in CSV format"
        list = [["Designator", "Val", "Package"]]
        with open(jlc_fn, "wt", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Comment", "Designator", "Footprint", "LCSC"])
            for (jlc_part, desc, footprint), identifiers in jlc_merged.items():
                w.writerow([desc, ",".join(identifiers), footprint, jlc_part])
        print("Saved JLC-format BOM to %s" % jlc_fn)

class Component:
    def __init__(self, identifier, footprint, value, pins=None, buses=None, desc=None, exclude_from_bom=False, partno=None, link=None, jlc_part=None):
        if pins is None: pins = []
        # autonumber identifiers
        if identifier.find("?") != -1:
            counter = 1
            while 1:
                maybe = identifier.replace("?", str(counter))
                if maybe not in pcb().components:
                    identifier = maybe
                    break
                counter += 1
        self.identifier = identifier
        assert self.identifier not in pcb().components, "identifier %s is already taken" % self.identifier
        pcb().components[self.identifier] = self

        self.footprint = footprint
        self.partno = partno
        self.link = link
        self.jlc_part = jlc_part
        if desc:
            self.desc = desc
        elif self.partno and self.link:
            self.desc = "%s; %s" % (self.partno, self.link)
        else:
            self.desc = ""
        self.exclude_from_bom = exclude_from_bom
        self.value = value
        self.buses = buses

        if type(pins) == type({}):
            pins = [
                Pin(pin_id, "", pin_nets)
                for pin_id, pin_nets in sorted(pins.items())
            ]

        self.pins = pins
        seen_pins = {}
        for pin in self.pins:
            if pin.number in seen_pins:
                raise Exception("Pin %s seen twice" % pin.number)
            seen_pins[pin.number] = pin
            print("- Add pin %s to component %s nets %s" % (pin.number, self.identifier, repr(pin.nets)))
            pin.component = self
            for net in pin.nets:
                if not net: continue  # ignore net ""
                pcb().nets.setdefault(net, []).append(pin)
                #print("  - Add net %s to %s.%s" % (net, self.identifier, pin.number))

    def xilinx_pins_by_net(self):
        r = {}
        for pin in self.pins:
            for net in pin.nets:
                if self.buses:
                    for bus in self.buses:
                        if net.startswith(bus):
                            net = "%s<%s>" % (net[:len(bus)], net[len(bus):])
                r.setdefault(net, []).append(pin.number)
        return r

class Pin:
    def __init__(self, number, name, nets=None):
        if nets is None: nets = []
        if type(nets) == type(""): nets = [nets]
        assert type(nets) == type([]), "invalid argument to nets: %s" % repr(nets)
        self.number, self.name, self.nets = number, name, nets

# 0805 capacitor
def C0805(value, net1, net2, ref="C?", handsoldering=True, footprint=None, jlc_part=None):
    if not footprint:
        footprint = "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" if handsoldering else "Capacitor_SMD:C_0805_2012Metric"
    if not jlc_part:
        jlc_part = {
            "100n": "C49678",
            "1u": "C28323",
        }.get(value, None)
    return Component(
        footprint=footprint,
        identifier=ref,
        value=value,
        jlc_part=jlc_part,
        desc="Capacitor 0805: %s" % value,
        pins=[
            Pin(1, "1", [net1]),
            Pin(2, "2", [net2]),
        ],
    )

# 0402 capacitor
def C0402(value, net1, net2, ref="C?"):
    return Component(
        footprint="Capacitor_SMD:C_0402_1005Metric",
        identifier=ref,
        value=value,
        desc="Capacitor 0402: %s" % value,
        pins=[
            Pin(1, "1", [net1]),
            Pin(2, "2", [net2]),
        ],
    )

# 0805 resistor
def R0805(value, net1, net2, ref="R?", handsoldering=True, jlc_part=None):
    if not jlc_part:
        jlc_part = {
            "0R": "C17477",
            "68R": "C17802",
            "330R": "C17630",
            "1k": "C17513",
            "2k2": "C17520",
            "4k7": "C17673",
            "10k": "C17414",
            "100k": "C17407",
        }.get(value, None)
    return Component(
        footprint="Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" if handsoldering else "Resistor_SMD:R_0805_2012Metric",
        identifier=ref,
        value=value,
        jlc_part=jlc_part,
        desc="Resistor 0805: %s" % value,
        pins=[
            Pin(1, "1", [net1]),
            Pin(2, "2", [net2]),
        ],
    )

# SOD-323 diode
def D(value, net_cathode, net_anode, footprint, package, ref="D?", jlc_part=None):
    return Component(
        footprint=footprint,
        identifier=ref,
        value=value,
        jlc_part=jlc_part,
        desc="Diode %s: %s" % (package, value),
        pins=[
            Pin(1, "1", net_cathode),
            Pin(2, "2", net_anode),
        ],
    )

def DSOD123(value, *args, **kwargs):
    return D(value, *args, footprint="Diode_SMD:D_SOD-123", package="SOD123", **kwargs)

def DSOD323(value, *args, **kwargs):
    assert 'bat54' not in value.lower(), "BAT54 is SOD123, not SOD323"  # I've made this mistake...
    return D(value, *args, footprint="Diode_SMD:D_SOD-323_HandSoldering", package="SOD323", **kwargs)

def LED0805(value, *args, **kwargs):
    return D(value, *args, footprint="LED_SMD:LED_0805_2012Metric", package="0805", **kwargs)

def pin_to_loc(pin_id):
    if type(pin_id) == types.IntType:
        return "P%d" % pin_id
    return pin_id

def update_xilinx_constraints(xilinx, fn):
    print("Updating constraints file %s" % fn)
    changed = False
    lines = []
    seen = set()
    nets = xilinx.xilinx_pins_by_net()
    for line in open(fn):
        line = line.rstrip()
        m = re.search(r"^NET (.*?) LOC = (.*?);$", line)
        if m:
            net = m.group(1)
            pin = m.group(2)
            seen.add(net)
            if net not in nets:
                print("WARNING: unknown net specified in Xilinx constraints line: %s" % line)
            elif len(nets[net]) > 1:
                print("WARNING: more than one pin assigned to Xilinx net %s" % net)
            elif nets[net][0] == pin:
                print("OK: pin %s is still assigned to Xilinx net %s" % (pin, net))
            else:
                pin_id = nets[net][0]
                print("CHANGED: Xilinx net %s is now on pin %s" % (net, pin_id))
                line = "NET %s LOC = %s;" % (net, pin_to_loc(pin_id))
                changed = True
        lines.append(line)
    for net, pins in sorted(nets.items()):
        if net in seen:
            continue
        if net in ('3V3', 'GND', 'cpld_TCK', 'cpld_TDO', 'cpld_TDI', 'cpld_TMS'):
            continue
        if len(pins) > 1:
            print("WARNING: can't add net %s to Xilinx constraints file because it's connected to more than one pin: %s" % (net, repr(pins)))
        else:
            print("CHANGED: Add Xilinx net %s (pin %s) to constraints file" % (net, pins[0]))
            lines.append("NET %s LOC = %s;" % (net, pin_to_loc(pins[0])))
            changed = True
    if changed:
        f = open(fn, 'w')
        for line in lines:
            print(line, file=f)
        print("Xilinx constraints updated in %s" % fn)

def check_xc9500xl_pinout(xilinx, cpld_path, project_name):
    print("Checking Xilinx XC9500XL series pinout against fitter output")
    fitter_report_fn = os.path.join(cpld_path, '%s_html/fit')
