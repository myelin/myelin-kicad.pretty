from myelin_kicad_mod import *

# Based on land pattern in https://www.mouser.com/datasheet/2/54/ATCAY-777361.pdf

X = Module(
	identifier="bourns_cat16_j8_resistor_array",
	description="Bourns CAT16-J8 resistor array (8 isolated resistors, 0.8mm pitch, concave)",
	ref_x=-2.5,
	ref_y=0,
	value_x=2.5,
	value_y=0,
	ref_rotate=90,
	value_rotate=90,
)

# Number of resistors
N_RES = 8

# Values from datasheet
a = 0.8
b = 0.425
p = 0.8
f = 2.6

SOLDERING_MARGIN_OUT = 0
SOLDERING_MARGIN_IN = 0

N = N_RES * 2

# plastic chip dimensions
D = a # chip height (ish)
E = p * N_RES + (p - b) * 2 # chip width
D1 = f # chip height including pads

# pin 1 is at the center of the top edge of the chip, and numbering proceeds counter clockwise
# pin 1 ID is a bubble below pin 1
PIN_SPACING = p
PAD_WIDTH = b

# draw outline
X.add(Line(-D/2, -E/2, -D/2, E/2)) # left
X.add(Line(-D/2, E/2, D/2, E/2)) # bottom
X.add(Line(D/2, E/2, D/2, -E/2)) # right
X.add(Line(D/2, -E/2, -D/2, -E/2)) # top

# pad width and height
w = (D1 - D) / 2 + SOLDERING_MARGIN_IN + SOLDERING_MARGIN_OUT
h = PAD_WIDTH
x_center = ((D + D1) / 2 + SOLDERING_MARGIN_OUT) / 2

### down the left edge and up the right edge
for pin in range(N/2):
	# left
	X.add(Pad(name="%dA" % (pin+1), x=-x_center, y=(pin - N/4 + 0.5) * PIN_SPACING, w=w, h=h))
	# right
	X.add(Pad(name="%dB" % (pin+1), x=x_center, y=(pin - N/4 + 0.5) * PIN_SPACING, w=w, h=h))

X.save()
