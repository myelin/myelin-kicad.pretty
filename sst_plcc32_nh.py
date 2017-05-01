from myelin_kicad_mod import *

# SST 32-pin PLCC NH package, e.g. for SST39SF010A-*-NHE
X = Module(
	identifier="sst_plcc32_nh",
	description="SST PLCC32 NH package - 0.450 x 0.550 in PLCC 0.05 in pitch"
)

SOLDERING_MARGIN_OUT = 1 # extend everything out for ease of soldering
SOLDERING_MARGIN_IN = 0 # extend underneath the chip a bit to soak up solder

# 32 pins
N = 32

# plastic chip dimensions
D = 0.450 * INCH
E = 0.550 * INCH
# including leads: 0.04" (1mm) extra
D1 = 0.490 * INCH
E1 = 0.590 * INCH

# pin 1 is at the center of the top edge of the chip, and numbering proceeds counter clockwise
# pin 1 ID is a bubble below pin 1
PIN_SPACING = 0.05 * INCH
PAD_WIDTH = 0.032 * INCH # 0.026-0.032"

# draw outline
X.add(Line(-D/2, -E/2 + 1, -D/2, E/2)) # left
X.add(Line(-D/2, E/2, D/2, E/2)) # bottom
X.add(Line(D/2, E/2, D/2, -E/2)) # right
X.add(Line(D/2, -E/2, -D/2 + 1, -E/2)) # top
X.add(Line(-D/2 + 1, -E/2, -D/2, -E/2 + 1)) # chopped corner

# draw pin 1 ID bubble
X.add(Circle(0, -E/2 + 1.5, 0.5))

# pad width and height (along the top row)
w = PAD_WIDTH
h = (E1-E) / 2 + SOLDERING_MARGIN_IN + SOLDERING_MARGIN_OUT

### pins 5-13 down the left edge.
for pin in range(9):
	X.add(Pad(name=pin+5, x=-D/2, y=(pin - 4) * PIN_SPACING, w=h, h=w))

### pins 14-20 along the bottom edge.
for pin in range(7):
	X.add(Pad(name=pin+14, x=(pin - 3) * PIN_SPACING, y=E/2, w=w, h=h))

### pins 21-29 up the right edge.
for pin in range(9):
	X.add(Pad(name=pin+21, x=D/2, y=(4 - pin) * PIN_SPACING, w=h, h=w))

### pins 30-32, 1-4 right to left along the top edge.
for pin in range(7):
	X.add(Pad(name=((pin + 29) % N) + 1, x=(3 - pin) * PIN_SPACING, y=-E/2, w=w, h=h))

X.save()
