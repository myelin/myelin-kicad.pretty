from myelin_kicad_mod import *

# Digikey ED1543-ND
# http://www.on-shore.com/wp-content/uploads/2015/09/302-sxxx.pdf

PINS_X, PINS_Y = 5, 2

# big holes for header pins
PAD_DIA = 0.060 * INCH
HOLE_DIA = 0.040 * INCH

SPACING = 2.54

PI_WIDTH = PINS_X * SPACING
PI_HEIGHT = PINS_Y * SPACING

MARGIN_X = (10.16 - 2.54)
MARGIN_Y = (9.10 - PI_HEIGHT)

OUTLINE_WIDTH = PI_WIDTH + MARGIN_X
OUTLINE_HEIGHT = PI_HEIGHT + MARGIN_Y

X = Module(
    identifier="jtag_shrouded_%dx%d" % (PINS_Y, PINS_X),
    description="100mil 2x5 header for JTAG -- Digikey ED1543-ND",
    ref_x=OUTLINE_WIDTH/2 - 2,
    ref_y=0,
    ref_rotate=90,
    value_x=-OUTLINE_WIDTH/2 + 2,
    value_y=0,
    value_rotate=90,
)

# outline
X.add(Line(-OUTLINE_WIDTH/2, -OUTLINE_HEIGHT/2, OUTLINE_WIDTH/2,  -OUTLINE_HEIGHT/2))
X.add(Line(-1.5, OUTLINE_HEIGHT/2, -1.5, OUTLINE_HEIGHT/2 - 1))  # notch edge
X.add(Line(-1.5, OUTLINE_HEIGHT/2 - 1, 1.5, OUTLINE_HEIGHT/2 - 1))  # notch
X.add(Line(1.5, OUTLINE_HEIGHT/2, 1.5, OUTLINE_HEIGHT/2 - 1))  # notch edge
X.add(Line(OUTLINE_WIDTH/2, OUTLINE_HEIGHT/2, OUTLINE_WIDTH/2, -OUTLINE_HEIGHT/2))
X.add(Line(OUTLINE_WIDTH/2, OUTLINE_HEIGHT/2, -OUTLINE_WIDTH/2, OUTLINE_HEIGHT/2))
X.add(Line(-OUTLINE_WIDTH/2, OUTLINE_HEIGHT/2, -OUTLINE_WIDTH/2, -OUTLINE_HEIGHT/2))

# pin 1 is bottom left
PIN1_X = -(float(PINS_X - 1) / 2 * SPACING)
PIN1_Y = (float(PINS_Y - 1) / 2 * SPACING)

print "making header with w=%d h=%d" % (PINS_X, PINS_Y)
for pin_x in range(PINS_X):
    for pin_y in range(PINS_Y):
        X.add(Pin(
            name=str(pin_x * PINS_Y + pin_y + 1),
            x=PIN1_X + SPACING * pin_x,
            y=PIN1_Y - SPACING * pin_y,
            dia=PAD_DIA,
            hole_dia=HOLE_DIA,
            square=(pin_x == 0 and pin_y == 0)
        ))

X.save()
