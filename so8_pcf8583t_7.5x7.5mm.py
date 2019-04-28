from myelin_kicad_mod import *

X = Module(
	identifier="so8_pcf8583t_7.5x7.5mm",
	description="7.5mm x 7.5mm SO8 for PCF8583T"
)

SOLDERING_MARGIN_OUT = 0.5 # extend everything out for ease of soldering
SOLDERING_MARGIN_IN = 0 # extend underneath the chip a bit to soak up solder

# pin count
N = 8

# plastic chip dimensions
D = 7.5 # width (E)
E = 7.5 # height (D)
# including leads
D1 = 10.65 # width (HE)

PIN_SPACING = 1.27
PIN_WIDTH = 0.425
PAD_WIDTH = 0.7  # a little extra for soldering

# draw outline
X.add(Line(-D/2, -E/2 + 1, -D/2, E/2)) # left
X.add(Line(-D/2, E/2, D/2, E/2)) # bottom
X.add(Line(D/2, E/2, D/2, -E/2)) # right
X.add(Line(D/2, -E/2, -D/2 + 1, -E/2)) # top
X.add(Line(-D/2 + 1, -E/2, -D/2, -E/2 + 1)) # chopped corner

# draw pin 1 ID bubble
X.add(Circle(0, -E/2 + 0.5, 0.5))

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
