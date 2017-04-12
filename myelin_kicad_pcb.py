# This file generates KiCad netlist (.net) files directly from a
# Python script, that specifies all parts, connections, and
# footprints.

nets = {}
components = {}

# format list entry for dump_list()
def fmt_item(item):
    if type(item) == type(""):
        if item.find(" ") != -1:
            return '"%s"' % item.replace('"', "'") # munge
    return str(item)

# format python list into kicad netlist format
def dump_list(list):
    return "(%s)\n" % " ".join(
        dump_list(item) if type(item) == type([]) else fmt_item(item)
        for item in list)

# write netlist to disk
def dump_netlist(fn):
    export_components = []
    export_nets = []

    for identifier, component in sorted(components.items()):
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
    for net_id, pins in sorted(nets.items()):
        net_case_check.setdefault(net_id.lower(), set()).add(net_id)
        net_counter += 1
        print "=== %s ===" % net_id
        export_nodes = []
        for pin in pins:
            print "  - %s.%s (%s %s)" % (pin.component.identifier, pin.number, pin.component.value, pin.name)
            export_nodes.append(["node", ["ref", pin.component.identifier], ["pin", pin.number]])
        export_nets.append(["net", ["code", net_counter], ["name", net_id if net_id else "_default"]] + export_nodes)
        if len(export_nodes) == 1:
            nets_with_one_node.add(net_id)

    for net_id in nets_with_one_node:
        print "WARNING: net %s only has one attached node" % net_id

    bad_nets_exist = 0
    for net_ids in net_case_check.values():
        if len(net_ids) == 1:
            continue
        print "Inconsistent casing in nets: %s" % " ".join(net_ids)
        bad_nets_exist = 1
    if bad_nets_exist:
        raise Exception("Inconsistent net casing; see details above")

    print>>open(fn, "w"), dump_list([
        "export",
        ["version", "D"],
        ["components", export_components],
        ["nets", export_nets],
    ])

class Component:
    def __init__(self, identifier, footprint, value, pins):
        # autonumber identifiers
        if identifier.find("?") != -1:
            counter = 1
            while 1:
                maybe = identifier.replace("?", str(counter))
                if not components.has_key(maybe):
                    identifier = maybe
                    break
                counter += 1
        self.identifier = identifier
        assert not components.has_key(self.identifier), "identifier %s is already taken" % self.identifier
        components[self.identifier] = self

        self.footprint = footprint
        self.value = value

        self.pins = pins
        for pin in self.pins:
            pin.component = self
            for net in pin.nets:
                nets.setdefault(net, []).append(pin)

class Pin:
    def __init__(self, number, name, nets=None):
        if nets is None: nets = []
        if type(nets) == type(""): nets = [nets]
        assert type(nets) == type([]), "invalid argument to nets: %s" % `nets`
        self.number, self.name, self.nets = number, name, nets

# 0805 capacitor
def C0805(value, net1, net2, ref="C?"):
    return Component(
        footprint="Capacitors_SMD:C_0805_HandSoldering",
        identifier=ref,
        value=value,
        pins=[
            Pin(1, "1", [net1]),
            Pin(2, "2", [net2]),
        ],
    )

# 0805 resistor
def R0805(value, net1, net2):
    return Component(
        footprint="Resistors_SMD:R_0805_HandSoldering",
        identifier="R?",
        value=value,
        pins=[
            Pin(1, "1", [net1]),
            Pin(2, "2", [net2]),
        ],
    )
