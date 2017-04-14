from myelin_kicad_mod import *

# SST 32-pin PLCC NH package, e.g. for SST39SF010A-*-NHE
X = Module(
    identifier="raspberry_pi_zero_flipped",
    description="Footprint for Raspberry Pi Zero, mounted upside down",
    ref_x=0,
    ref_y=15,
    value_x=0,
    value_y=10,
)

# big holes for header pins
PAD_DIA = 0.070 * INCH
HOLE_DIA = 0.040 * INCH

# origin at the center of the top edge of the Pi Zero module, so we'll go out to
# left=-32.5 and right=32.5, with top=0 and bottom=30
PI_WIDTH = 65.0
PI_HEIGHT = 30.0

# outline
X.add(Line(-PI_WIDTH/2, 0, PI_WIDTH/2,  0))
X.add(Line(PI_WIDTH/2, 0, PI_WIDTH/2, PI_HEIGHT))
X.add(Line(PI_WIDTH/2, PI_HEIGHT, -PI_WIDTH/2, PI_HEIGHT))
X.add(Line(-PI_WIDTH/2, PI_HEIGHT, -PI_WIDTH/2, 0))

# NPTH drill holes
X.add(Hole(-PI_WIDTH/2 + 3.5, 3.5, hole_dia=2.5))
X.add(Hole(PI_WIDTH/2 - 3.5, 3.5, hole_dia=2.5))
X.add(Hole(-PI_WIDTH/2 + 3.5, PI_HEIGHT - 3.5, hole_dia=2.5))
X.add(Hole(PI_WIDTH/2 - 3.5, PI_HEIGHT - 3.5, hole_dia=2.5))

PINS_X = 20 # cols
PINS_Y = 2 # rows
SPACING = 2.54

# pin 2 is right on the top border, on the RHS, so 24.13, 2.23
# pin 1 is below that, so 24.13, 4.77
PIN1_X = (float(PINS_X - 1) / 2 * SPACING)
PIN1_Y = 3.5 + SPACING/2
assert PIN1_X == 24.13
assert PIN1_Y == 4.77

# pin 40 should be -24.13, 2.23

for pin_x in range(PINS_X):
    for pin_y in range(PINS_Y):
        X.add(Pin(
            name=str(pin_x * PINS_Y + pin_y + 1),
            x=PIN1_X - SPACING * pin_x,
            y=PIN1_Y - SPACING * pin_y,
            dia=PAD_DIA,
            hole_dia=HOLE_DIA,
            square=(pin_x == 0 and pin_y == 0)
        ))

X.save()
