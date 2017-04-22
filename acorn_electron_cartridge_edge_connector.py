from myelin_kicad_mod import *

X = Module(
	identifier="acorn_electron_cartridge_edge_connector",
	description="Edge connector for an Acorn Electron Plus 1 cartridge (top layer = rear of Plus 1)",
	ref_x=-21,
	ref_y=-7,
	value_x=7,
	value_y=-7,
)
X.add(Text(-15, -7, "rear"))
X.add(Text(-15, -7, "front", bottom=True))

# 44 connectors, 0.1" spacing
N = 44
PAD_SPACING = 2.54

# - MartinB says 57mm is about right for the cartridge connector
# - My PCBs using PaulB's cartridge are slightly narrower than 
#   the Plus 1 socket, so bumping it up from there would be nice.
# - From acorn_electron_cartridge_socket.py:
#   C = card slot width = 2.3" = 58.42
# - I took some measurements from a Hopper ROM PCB:
#   http://www.stardot.org.uk/forums/viewtopic.php?f=3&t=12815&sid=657881ef80e2a1f0ad344db906e2f12f#p166861
#   The board in there is 2.25" (57.15 mm) wide, so 57mm should be
#   just about perfect.

CONNECTOR_WIDTH = 57.0
CHAMFER = 1

# When installed in an Electron, the bottom 31mm of PCB are inside the Plus 1
PLUS_1_DEPTH = 31.0

# Connector pads
PAD_W = 1.27
PAD_H = 11.0

# Depth line
X.add(Line(-CONNECTOR_WIDTH/2, -PLUS_1_DEPTH + PAD_H, CONNECTOR_WIDTH/2, -PLUS_1_DEPTH + PAD_H))
#X.add(Text(0, -PLUS_1_DEPTH + PAD_H + 2, "Everything below this line is inside the Plus 1"))


# label far left and right pins
# pin A1 and B1 are 5V
X.add(Text(-10.5 * PAD_SPACING, -7, "5V"))
X.add(Text(-10.5 * PAD_SPACING, -7, "5V", bottom=True))
# pin A22 and B22 are 0V
X.add(Text(10.5 * PAD_SPACING, -7, "0V"))
X.add(Text(10.5 * PAD_SPACING, -7, "0V", bottom=True))

# left side
X.add(Line(-CONNECTOR_WIDTH/2, -PAD_H/2, -CONNECTOR_WIDTH/2, PAD_H/2 - CHAMFER, layers=EDGE))
# left chamfer
X.add(Line(-CONNECTOR_WIDTH/2, PAD_H/2 - CHAMFER, -CONNECTOR_WIDTH/2 + CHAMFER, PAD_H/2, layers=EDGE))
# bottom
X.add(Line(-CONNECTOR_WIDTH/2 + CHAMFER, PAD_H/2, CONNECTOR_WIDTH/2 - CHAMFER, PAD_H/2, layers=EDGE))
# right chamfer
X.add(Line(CONNECTOR_WIDTH/2 - CHAMFER, PAD_H/2, CONNECTOR_WIDTH/2, PAD_H/2 - CHAMFER, layers=EDGE))
# right side
X.add(Line(CONNECTOR_WIDTH/2, PAD_H/2 - CHAMFER, CONNECTOR_WIDTH/2, -PAD_H/2, layers=EDGE))

# From AN14:
# Pin 22                  Pin 1
# ----------------------------- Side "A"
# ----------------------------- Side "B"
#             (front)

# This footprint puts the "A" row of pins on the front layer, as in PaulB's
# AcornElectronCartridge.pretty, because Plus 1 cartridges typically put all
# the components on the A-side (so the top layer of the PCB faces away from
# the user when plugged into an Electron, and the bottom layer faces towards
# the user).  As such, the pin numbering is from left to right.

for pin in range(N/2):
	x = (pin - float(N/2 - 1)/2) * PAD_SPACING
	y = 0
	X.add(Pad(name="A%d" % (pin+1), x=x, y=y, w=PAD_W, h=PAD_H, layers=FRONT_PAD))
	X.add(Pad(name="B%d" % (pin+1), x=x, y=y, w=PAD_W, h=PAD_H, layers=BACK_PAD))

X.save()
