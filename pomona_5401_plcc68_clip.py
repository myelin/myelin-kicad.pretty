from myelin_kicad_mod import *

X = Module(
    identifier="pomona_5401_plcc68_clip",
    description="test clip for 68-plcc",
    ref_x=0,
    ref_y=0.1 * INCH,
    value_x=0,
    value_y=-0.1 * INCH,
)

N_PINS = 68

# Not in any datasheet, just measured and tweaked until the footprint matches.
# Initial measurement was 31mm (1.22") but that resulted in holes slightly too close together.
# We want the holes here to be slightly closer together so we can straighten the pins and press down to connect.
# 1.2" is nice because it has everything on a 100mil grid.
LINE_POS = 1.20 * INCH / 2

# big holes for header pins
PAD_DIA = 0.060 * INCH
HOLE_DIA = 0.040 * INCH

SPACING = 2.54

OUTLINE_POS = LINE_POS + 0.1 * INCH

# pins on each edge zig zag (rows offset by 1.27mm)
# and outer rows are 1.22" apart
# i.e. rows/cols are at -1.22/2, -1.12/2, 1.12/2, 1.22/2

# pin 1 is top center at (0, 1.22/2), and pins proceed anticlockwise

for realpin in range(1, N_PINS + 1):
    # to make the math easier,rotate 9 pins right, so pin 0 is the top pin on the left hand side
    easypin = (realpin - int(float(N_PINS) / 8 + 0.5) - 1 + N_PINS) % N_PINS

    # also normalize to one side then rotate
    normpin = easypin % (N_PINS / 4)
    x = -LINE_POS + (SPACING if normpin % 2 else 0)
    y = (normpin - int(float(N_PINS)/8)) * SPACING/2

    # rotate now
    group = int(easypin / (N_PINS / 4))
    for _ in range(group):
        x, y = y, -x

    print "real pin %d, easy pin %d, normpin %d, group %d" % (realpin, easypin, normpin, group)

    X.add(Pin(
        name=str(realpin),
        x=x,
        y=y,
        dia=PAD_DIA,
        hole_dia=HOLE_DIA,
        square=(realpin == 1)
    ))

# outline
X.add(Line(-OUTLINE_POS, -OUTLINE_POS, OUTLINE_POS,  -OUTLINE_POS))
X.add(Line(OUTLINE_POS, OUTLINE_POS, OUTLINE_POS, -OUTLINE_POS))
X.add(Line(OUTLINE_POS, OUTLINE_POS, -OUTLINE_POS, OUTLINE_POS))
X.add(Line(-OUTLINE_POS, OUTLINE_POS, -OUTLINE_POS, -OUTLINE_POS))

# pin 1 ID bubble
X.add(Circle(0, -OUTLINE_POS - 0.05 * INCH, 0.05 * INCH))

X.save()
