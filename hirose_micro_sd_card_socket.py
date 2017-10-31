from myelin_kicad_mod import *

X = Module(
    identifier="hirose_micro_sd_card_socket",
    description="Hirose DM3D-SF micro SD card socket",
    ref_x=0,
    ref_y=7,
    value_x=0,
    value_y=8.5,
)

# Origin: x = center of card, y = top of socket.

# The socket is 11.95 x 11.45 mm
OUTLINE_WIDTH = 11.95
OUTLINE_LEFT = -OUTLINE_WIDTH/2
OUTLINE_RIGHT = OUTLINE_WIDTH/2
OUTLINE_TOP = 0
OUTLINE_BASE = OUTLINE_TOP + 10.2  # lots of things are measured from here
OUTLINE_BOTTOM = 11.45
SD_CARD_WIDTH = 11
SD_CARD_CENTER = OUTLINE_RIGHT - 6  # just barely left of center
SD_CARD_RIGHT = SD_CARD_CENTER + 5.5
SD_CARD_LEFT = SD_CARD_CENTER - 5.5
SD_CARD_BOTTOM = OUTLINE_TOP + 15.8

# outline of SD card socket
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_TOP))
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_LEFT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_LEFT, OUTLINE_BOTTOM, OUTLINE_RIGHT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_RIGHT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_BOTTOM))
# and an SD card protruding
X.add(Line(SD_CARD_LEFT, OUTLINE_BOTTOM, SD_CARD_LEFT, SD_CARD_BOTTOM))
X.add(Line(SD_CARD_LEFT, SD_CARD_BOTTOM, SD_CARD_RIGHT, SD_CARD_BOTTOM))
X.add(Line(SD_CARD_RIGHT, SD_CARD_BOTTOM, SD_CARD_RIGHT, OUTLINE_BOTTOM))

# signal and power pads
PAD_WIDTH = 0.7
PAD_HEIGHT = 1.75

PADS_Y = OUTLINE_BASE + PAD_HEIGHT/2
# pads left of the centerline
PAD_8_X = SD_CARD_CENTER - 4.5
for pad_count in range(8):
	X.add(Pad(
		name=8-pad_count,
		x=PAD_8_X + 1.1*pad_count,
		y=PADS_Y,
		w=PAD_WIDTH,
		h=PAD_HEIGHT,
	))

# card detect pads
# card detect B (left)
px, pw = x_width_from_lr(PAD_8_X - 1.85, PAD_8_X - 0.4)
X.add(Pad(name="CDB", x=px, y=OUTLINE_BASE - 8.35, w=pw, h=1))
# card detect A (right)
py, ph = x_width_from_lr(OUTLINE_BASE - 9.15, OUTLINE_BASE - 10.7)
X.add(Pad(name="CDA", x=PAD_8_X + 10.9 - 0.8, y=py, w=1, h=ph))

# one mounting/ground pad on either side
SHIELD_PAD_HEIGHT = 1.5
SHIELD_PAD_Y = OUTLINE_BASE + SHIELD_PAD_HEIGHT/2
# bottom left pad
px, pw = x_width_from_lr(PAD_8_X - 1.85, PAD_8_X - 0.55)
X.add(Pad(name="SH1", x=px, y=SHIELD_PAD_Y, w=pw, h=SHIELD_PAD_HEIGHT))
# bottom right pad
px, pw = x_width_from_lr(PAD_8_X + 9.4, PAD_8_X + 10.9)
X.add(Pad(name="SH2", x=px, y=SHIELD_PAD_Y, w=pw, h=SHIELD_PAD_HEIGHT))
# top left pad
px, pw = x_width_from_lr(PAD_8_X - 1.85, PAD_8_X - 1.85 + 0.8)
py = OUTLINE_BASE - 6.85
ph = 1.5
X.add(Pad(name="SH3", x=px, y=py, w=pw, h=ph))
# top right pad
px, pw = x_width_from_lr(PAD_8_X + 10.9, PAD_8_X + 10.9 - 0.8)
py = OUTLINE_BASE - 7.5
ph = 1.4
X.add(Pad(name="SH4", x=px, y=py, w=pw, h=ph))

# keep out zones
X.add(Text(x=0, y=1, text="XX"))
X.add(Text(x=PAD_8_X + 8.1 - 8.5/2, y=OUTLINE_BASE - 5, text="XXXXXXXXX"))

X.save()
