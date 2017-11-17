from myelin_kicad_mod import *

X = Module(
    identifier="micro_usb_b_smd_molex",
    description="Molex SD-105017-001 bottom mount micro USB socket",
    ref_x=0,
    ref_y=1,
    value_x=0,
    value_y=-4,
)

# Orientation: PCB edge at bottom of socket, pins at top.
# Face up, so if you want the socket mounted "properly" (under the PCB), it'll need
# to go on the bottom component side.

# +----> X
# |
# |
# Y

# 5mm from pcb edge to back of socket, 4.7mm if excluding the pins that stick out the back.
# Socket extends past the PCB edge another 0.7mm.
OUTLINE_HEIGHT = 5
OUTLINE_BOTTOM = OUTLINE_HEIGHT / 2
OUTLINE_TOP = -OUTLINE_HEIGHT / 2
# 7.5mm from left to right; 8mm including bits that protrude to the sides past the PCB edge
OUTLINE_WIDTH = 8
OUTLINE_RIGHT = OUTLINE_WIDTH / 2
OUTLINE_LEFT = -OUTLINE_WIDTH / 2

PCB_EDGE_Y = OUTLINE_BOTTOM
SOCKET_FRONT_Y = PCB_EDGE_Y + 0.7  # front of socket (past the PCB edge)
MOUNTING_PINS_Y = PCB_EDGE_Y - 1.45  # mechanical mounting
ELEC_PINS_Y = MOUNTING_PINS_Y - 2.7  # two mounting pins + 5 electrical pads
ELEC_PINS_CENTER_X = 0

# outline of SD card socket
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_TOP))
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_LEFT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_LEFT, OUTLINE_BOTTOM, OUTLINE_RIGHT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_RIGHT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_BOTTOM))
# connector front
X.add(Line(OUTLINE_LEFT, SOCKET_FRONT_Y, OUTLINE_LEFT + 1, SOCKET_FRONT_Y))
X.add(Line(OUTLINE_RIGHT - 1, SOCKET_FRONT_Y, OUTLINE_RIGHT, SOCKET_FRONT_Y))

# signal and power pads
PAD_WIDTH = 0.4
PAD_HEIGHT = 1.35
PAD_EXTRA_HEIGHT = 0.5
PAD_SPACING = 0.65
TEXT_SIZE = 0.7

X.add(Pad(name="1", x=ELEC_PINS_CENTER_X - PAD_SPACING * 2, y=ELEC_PINS_Y - PAD_EXTRA_HEIGHT/2,
    w=PAD_WIDTH, h=PAD_HEIGHT + PAD_EXTRA_HEIGHT))
X.add(Text(ELEC_PINS_CENTER_X - PAD_SPACING * 2, ELEC_PINS_Y+1.5, text="V", size=TEXT_SIZE))
X.add(Pad(name="2", x=ELEC_PINS_CENTER_X - PAD_SPACING, y=ELEC_PINS_Y - PAD_EXTRA_HEIGHT/2,
    w=PAD_WIDTH, h=PAD_HEIGHT + PAD_EXTRA_HEIGHT))
X.add(Text(ELEC_PINS_CENTER_X - PAD_SPACING, ELEC_PINS_Y+1.5, "-", size=TEXT_SIZE))
X.add(Pad(name="3", x=ELEC_PINS_CENTER_X, y=ELEC_PINS_Y - PAD_EXTRA_HEIGHT/2,
    w=PAD_WIDTH, h=PAD_HEIGHT + PAD_EXTRA_HEIGHT))
X.add(Text(ELEC_PINS_CENTER_X, ELEC_PINS_Y+1.5, "+", size=TEXT_SIZE))
X.add(Pad(name="4", x=ELEC_PINS_CENTER_X + PAD_SPACING, y=ELEC_PINS_Y - PAD_EXTRA_HEIGHT/2,
    w=PAD_WIDTH, h=PAD_HEIGHT + PAD_EXTRA_HEIGHT))
X.add(Text(ELEC_PINS_CENTER_X + PAD_SPACING, ELEC_PINS_Y+1.5, "I", size=TEXT_SIZE))
X.add(Pad(name="5", x=ELEC_PINS_CENTER_X + PAD_SPACING * 2, y=ELEC_PINS_Y - PAD_EXTRA_HEIGHT/2,
    w=PAD_WIDTH, h=PAD_HEIGHT + PAD_EXTRA_HEIGHT))
X.add(Text(ELEC_PINS_CENTER_X + PAD_SPACING * 2, ELEC_PINS_Y+1.5, "G", size=TEXT_SIZE))

# mounting pins in line with electrical pads
X.add(Pin(name="P0", x=ELEC_PINS_CENTER_X - 2.5, y=ELEC_PINS_Y, dia=1.45, hole_dia=0.85))
X.add(Pin(name="P1", x=ELEC_PINS_CENTER_X + 2.5, y=ELEC_PINS_Y, dia=1.45, hole_dia=0.85))

# mounting pins between electrical pads and socket front
X.add(Pin(name="M0", x=ELEC_PINS_CENTER_X - 3.5, y=MOUNTING_PINS_Y, dia=1.9, hole_dia=1.3))
X.add(Pin(name="M1", x=ELEC_PINS_CENTER_X + 3.5, y=MOUNTING_PINS_Y, dia=1.9, hole_dia=1.3))

X.save()
