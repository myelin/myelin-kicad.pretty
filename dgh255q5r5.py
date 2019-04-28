from myelin_kicad_mod import *

for part_id, length, width, lead_spacing, lead_dia in [
    ["dgh255q5r5", 21.0, 11.0, 15.5, 0.6],
]:
    X = Module(
        identifier=part_id,
        description="%s supercapacitor" % part_id,
        ref_x=10,
        ref_y=3.81,
        value_x=-10,
        value_y=3.81,
    )

    
    # 25 mil header pins are 25*1.4142 = 35.355 mil (0.898 mm) across,
    # and fit in a 40 mil (1.016 mm) hole, i.e. 0.118 mm clearance.
    # As such let's ass 0.12 mm to our lead diameter to get a decent
    # hole size.
    HOLE_DIA = lead_dia + 0.12

    # 0.5 mm extra for soldering -- 0.25mm ring
    PAD_DIA = HOLE_DIA + 0.5

    PI_WIDTH = length
    PI_HEIGHT = width

    # outline
    X.add(Line(-PI_WIDTH/2, -PI_HEIGHT/2, PI_WIDTH/2,  -PI_HEIGHT/2))
    X.add(Line(PI_WIDTH/2, PI_HEIGHT/2, PI_WIDTH/2, -PI_HEIGHT/2))
    X.add(Line(PI_WIDTH/2, PI_HEIGHT/2, -PI_WIDTH/2, PI_HEIGHT/2))
    X.add(Line(-PI_WIDTH/2, PI_HEIGHT/2, -PI_WIDTH/2, -PI_HEIGHT/2))

    for pin_id, pin_x, pin_y in [
        ("1", -lead_spacing/2, 0),
        ("2", lead_spacing/2, 0),
        ]:
        X.add(Pin(
                name=pin_id,
                x=pin_x,
                y=pin_y,
                dia=PAD_DIA,
                hole_dia=HOLE_DIA,
                square=(pin_id == "1")
                ))

    X.save()
