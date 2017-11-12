from myelin_kicad_mod import *

# footprint for BBC Master Econet Module

X = Module(
	identifier="bbc_master_econet_module",
	description="BBC Master Econet Module 01-ADF10 pin landing pattern"
)

# pad and hole diameters
PAD_DIA = 0.070 * INCH
HOLE_DIA = 0.040 * INCH

# two rows of pins, 44mm separated vertically
HEIGHT = 44
WIDTH = 1.7 * INCH

# top row: 5 pins
for pin in range(5):
	X.add(Pin(
        "E%d" % (pin + 1),
        (pin + 10) * 0.1 * INCH - WIDTH/2,
        -HEIGHT/2,
        PAD_DIA,
        HOLE_DIA,
        square=(pin == 0)))

# bottom row: 17 pins
for pin in range(17):
	X.add(Pin(
        pin + 1,
        pin * 0.1 * INCH - WIDTH/2,
        HEIGHT/2,
        PAD_DIA,
        HOLE_DIA,
        square=(pin == 0)))

X.save()
