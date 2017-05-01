from myelin_kicad_mod import *

X = Module(
	identifier="issi_32l_450mil_sop",
	description="ISSI 32-pin 450mil SOP - e.g. for IS62C1024AL-QLI"
)

SOLDERING_MARGIN_OUT = 1 # extend everything out for ease of soldering
SOLDERING_MARGIN_IN = 0 # extend underneath the chip a bit to soak up solder

# 32 pins
N = 32

# plastic chip dimensions
D = 0.445 * INCH # width (E1)
E = 0.807 * INCH # height (D)
# including leads: 0.04" (1mm) extra
D1 = 0.556 * INCH # width (E)

# pin 1 is at the center of the top edge of the chip, and numbering proceeds counter clockwise
# pin 1 ID is a bubble below pin 1
PIN_SPACING = 1.27
PIN_WIDTH = 0.51
PAD_WIDTH = 0.7
# need at least 21 mil / 0.5334 mm between pads so we can get a trace through, so max pad width = 0.7366

# draw outline
X.add(Line(-D/2, -E/2 + 1, -D/2, E/2)) # left
X.add(Line(-D/2, E/2, D/2, E/2)) # bottom
X.add(Line(D/2, E/2, D/2, -E/2)) # right
X.add(Line(D/2, -E/2, -D/2 + 1, -E/2)) # top
X.add(Line(-D/2 + 1, -E/2, -D/2, -E/2 + 1)) # chopped corner

# draw pin 1 ID bubble
#X.add(Circle(0, -E/2 + 1.5, 0.5))

# pad width and height
w = (D1 - D) / 2 + SOLDERING_MARGIN_IN + SOLDERING_MARGIN_OUT
h = PAD_WIDTH
x_center = ((D + D1) / 2 + SOLDERING_MARGIN_OUT) / 2

### down the left edge and up the right edge
for pin in range(N/2):
	# left
	X.add(Pad(name=pin+1, x=-x_center, y=(pin - N/4 + 0.5) * PIN_SPACING, w=w, h=h))
	# right
	X.add(Pad(name=pin+N/2+1, x=x_center, y=(N/4 - pin - 0.5) * PIN_SPACING, w=w, h=h))

X.save()
