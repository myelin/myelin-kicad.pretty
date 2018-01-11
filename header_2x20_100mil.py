from myelin_kicad_mod import *

for PINS_X, PINS_Y in [
    (20, 2),
    (10, 4),
    (6, 2),
    (7, 2),
]:
    X = Module(
        identifier="header_%dx%02d_100mil" % (PINS_Y, PINS_X),
        description="%dx%02d header, 2.54mm/100mil pin spacing" % (PINS_Y, PINS_X),
        ref_x=10,
        ref_y=3.81,
        value_x=-10,
        value_y=3.81,
    )

    # big holes for header pins
    PAD_DIA = 0.060 * INCH
    HOLE_DIA = 0.040 * INCH

    SPACING = 2.54

    PI_WIDTH = PINS_X * SPACING
    PI_HEIGHT = PINS_Y * SPACING

    # outline
    X.add(Line(-PI_WIDTH/2, -PI_HEIGHT/2, PI_WIDTH/2,  -PI_HEIGHT/2))
    X.add(Line(PI_WIDTH/2, PI_HEIGHT/2, PI_WIDTH/2, -PI_HEIGHT/2))
    X.add(Line(PI_WIDTH/2, PI_HEIGHT/2, -PI_WIDTH/2, PI_HEIGHT/2))
    X.add(Line(-PI_WIDTH/2, PI_HEIGHT/2, -PI_WIDTH/2, -PI_HEIGHT/2))

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
