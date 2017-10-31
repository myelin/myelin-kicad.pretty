from myelin_kicad_mod import *

X = Module(
    identifier="fci_sd_card_socket",
    description="FCI 10067847 SD card socket",
    ref_x=0,
    ref_y=-15,
    value_x=0,
    value_y=-10,
)

# The origin is right in between the two mounting holes, so the right hand one
# is at (12.10, 0) and the left hand one is at (-12.10, 0).
MOUNTING_HOLE_X = 12.10
MOUNTING_HOLE_Y = 0

# The socket is 28.5 x 29.0 mm, so this outline is (0.4 mm, 0.2 mm) larger
OUTLINE_LEFT = -14
OUTLINE_RIGHT = 14.9  # we center on the SD card, not the socket
OUTLINE_TOP = -23.7
OUTLINE_BOTTOM = 5.5
SD_CARD_EDGE_X = 24 / 2
SD_CARD_BOTTOM = OUTLINE_TOP + 35.4

# outline of SD card socket
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_TOP))
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_LEFT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_LEFT, OUTLINE_BOTTOM, OUTLINE_RIGHT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_RIGHT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_BOTTOM))
# and an SD card protruding
X.add(Line(-SD_CARD_EDGE_X, OUTLINE_BOTTOM, -SD_CARD_EDGE_X, SD_CARD_BOTTOM))
X.add(Line(-SD_CARD_EDGE_X, SD_CARD_BOTTOM,  SD_CARD_EDGE_X, SD_CARD_BOTTOM))
X.add(Line( SD_CARD_EDGE_X, SD_CARD_BOTTOM,  SD_CARD_EDGE_X, OUTLINE_BOTTOM))

# signal and power pads
PAD_WIDTH = 1
PAD_HEIGHT = 1.5

PADS_Y = -24.3
# pads left of the centerline
PAD_4_X = -0.625
PAD_5_X = PAD_4_X - 2.5
PAD_6_X = PAD_5_X - 2.5
PAD_7_X = PAD_6_X - 2.425
PAD_8_X = PAD_7_X - 1.7
PAD_WP_X = PAD_8_X - 3.35
# pads right of the centerline
PAD_3_X = 1.075
PAD_CD_X = PAD_3_X + 1.65
PAD_2_X = PAD_CD_X + 1.65
# right hand side
PAD_9_X = 9.375
PAD_1_X = PAD_9_X - 2.5
# check
assert PAD_9_X == PAD_6_X + 15, "pad 9 should be 15mm right of pad 6, actually %.2f" % (PAD_9_X - PAD_6_X)

X.add(Pad(name="WP", x=PAD_WP_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="8", x=PAD_8_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="7", x=PAD_7_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="6", x=PAD_6_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="5", x=PAD_5_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="4", x=PAD_4_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="3", x=PAD_3_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="CD", x=PAD_CD_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="2", x=PAD_2_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="1", x=PAD_1_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))
X.add(Pad(name="9", x=PAD_9_X, y=PADS_Y, w=PAD_WIDTH, h=PAD_HEIGHT))

# one mounting/ground pads on either side
SHIELD_PAD_WIDTH = 1.2
SHIELD_PAD_HEIGHT = 2.2
# left pad
X.add(Pad(name="SH1", x=-13 - SHIELD_PAD_WIDTH/2, y=-2.1, w=SHIELD_PAD_WIDTH, h=SHIELD_PAD_HEIGHT))
# right pad
X.add(Pad(name="SH2", x=13.8 + SHIELD_PAD_WIDTH/2, y=-3.3, w=SHIELD_PAD_WIDTH, h=SHIELD_PAD_HEIGHT))

# one mounting hole on either side
HOLE_DIA = 1.5
X.add(Hole(-MOUNTING_HOLE_X, MOUNTING_HOLE_Y, hole_dia=HOLE_DIA))
X.add(Hole( MOUNTING_HOLE_X, MOUNTING_HOLE_Y, hole_dia=HOLE_DIA))

X.save()
