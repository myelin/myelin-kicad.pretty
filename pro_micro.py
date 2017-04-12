from myelin_kicad_mod import *

# footprint for Sparkfun Pro Micro
# 2 rows x 12 pins

X = Module(
	identifier="pro_micro",
	description="Sparkfun Pro Micro ATMEGA32U4"
)

# pin count
N = 24

# orientation: USB port on left
# pin 1-12 left to right on the bottom row
# pin 13-24 right to left on the top row

# pad and hole diameters
PAD_DIA = 0.070 * INCH
HOLE_DIA = 0.040 * INCH

# distance between rows
ROW_SEP = 0.6 * INCH # VERIFY THIS
COL_SEP = 0.1 * INCH
WIDTH = (N/2 - 1) * COL_SEP

# bounding box
BOX_HEIGHT = 0.7 * INCH
BOX_WIDTH = 1.3 * INCH

# draw outline
X.add(Line(-BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2,  BOX_HEIGHT/2))
X.add(Line(-BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2,  BOX_HEIGHT/2))
X.add(Line( BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2, -BOX_HEIGHT/2))
X.add(Line( BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2, -BOX_HEIGHT/2))

X.add(Text(-BOX_WIDTH/2 + 2, 0, "USB", rotation=90))

for pin in range(N/2):
	# pins are shifted right 0.05" from expected spot bc there's an extra
	# empty pin spot on the far left
	x = -WIDTH / 2 + COL_SEP * (pin + 0.5)
	# top row: 24-13
	X.add(Pin(24 - pin, x, -ROW_SEP/2, PAD_DIA, HOLE_DIA))
	# bottom row: 1-12
	X.add(Pin(pin + 1, x, ROW_SEP/2, PAD_DIA, HOLE_DIA, square=(pin == 0)))

X.save()
