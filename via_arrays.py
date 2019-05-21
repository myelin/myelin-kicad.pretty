from myelin_kicad_mod import *

VIA_PAD = 0.032 * INCH
VIA_HOLE = 0.013 * INCH

def make_straight_module(N, SPACING, SPACING_STR=None, pad=VIA_PAD, hole=VIA_HOLE):
	X = Module(
		identifier="via_single" if N == 1 else "via_array_1x%d_%s" % (N, SPACING_STR),
		description="Via array for stapling planes together",
		silkscreen=False,
	)
	for i in range(N):
		X.add(Pin(
			name=i+1,
			x=0 if N==1 else (i - float(N)/2) * SPACING,
			y=0,
			dia=pad,
			hole_dia=hole,
			solid_connect=True,
			layers=["*.Cu"],
		))
	X.save()

def make_zigzag_module(N, SPACING, SPACING_STR=None):
	X = Module(
		identifier="via_zigzag_1x%d_%s" % (N, SPACING_STR),
		description="Via array for stapling planes together",
		silkscreen=False,
	)
	for i in range(N):
		X.add(Pin(
			name=i+1,
			x=(i - float(N)/2) * SPACING,
			y=-SPACING/2 if (i % 2) == 0 else SPACING/2,
			dia=VIA_PAD,
			hole_dia=VIA_HOLE,
			solid_connect=True,
			layers=["*.Cu"],
		))
	X.save()

make_straight_module(1, 2.54, "2.54mm")
make_straight_module(7, 0.055 * INCH, "55mil")
make_straight_module(22, 2.54, "2.54mm")
make_straight_module(51, 1.0, "1mm", pad=0.6, hole=0.3)
make_zigzag_module(44, 1.27, "1.27mm")
