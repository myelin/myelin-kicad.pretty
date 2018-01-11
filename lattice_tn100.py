from myelin_kicad_mod import *

X = Module(
	identifier="lattice_tn100",
	description=(
		"Lattice TN100 - 14x14mm TQFP100 0.5mm pitch - "
		"https://www.latticesemi.com/~/media/LatticeSemi/Documents/PinPackage/PackageDiagrams.pdf?document_id=213")
)

SOLDERING_MARGIN_OUT = 1 # extend everything out for ease of soldering
SOLDERING_MARGIN_IN = 0 # extend underneath the chip a bit to soak up solder

# number of pins
N = 100

# plastic chip is 14 x 14 mm
D = E = 14.0
# including leads it's 16 mm x 16 mm (so leads are 1 mm long)
D1 = E1 = 16.0

# pin 1 is at the top of the left edge of the chip, and numbering proceeds counter clockwise
# pin 1 ID is a bubble in the top left corner
PIN_SPACING = 0.5
PIN_WIDTH = 0.22 # 'b' on the spec
PAD_WIDTH = 0.25 # just barely wider than the pin, allowing 0.25mm (9.8 mil) between pads

# draw outline
X.add(Line(-D/2, -E/2, -D/2, E/2))
X.add(Line(-D/2, E/2, D/2, E/2))
X.add(Line(D/2, E/2, D/2, -E/2))
X.add(Line(D/2, -E/2, -D/2, -E/2))

# draw pin 1 ID bubble
X.add(Circle(-D/2 + 0.5, -E/2 + 0.5, 0.25))

# work out positive distances out to the most clockwise pin in a line
x1 = D / 2 - SOLDERING_MARGIN_IN
x0 = D1 / 2 + SOLDERING_MARGIN_OUT
x = (x0 + x1) / 2
w = abs(x0 - x1)
y = (float(N) / 4 - 1) / 2 * PIN_SPACING
h = PAD_WIDTH

### pins 1-11 down the left edge.  x neg, y neg -> pos
for pin in range(N/4):
	X.add(Pad(name=pin+1, x=-x, y=-y + pin * PIN_SPACING, w=w, h=h))

### pins 12-22 along the bottom edge.  x neg -> pos, y pos
for pin in range(N/4):
	X.add(Pad(name=pin+N/4+1, x=-y + pin * PIN_SPACING, y=x, w=h, h=w))

### pins 23-33 up the right edge.  x pos, y pos -> neg
for pin in range(N/4):
	X.add(Pad(name=pin+N/2+1, x=x, y=y - pin * PIN_SPACING, w=w, h=h))

### pins 34-44 right to left along the top edge.  x pos -> neg, y neg
for pin in range(N/4):
	X.add(Pad(name=pin+3*(N/4)+1, x=y - pin * PIN_SPACING, y=-x, w=h, h=w))

X.save()
