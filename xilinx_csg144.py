from myelin_kicad_mod import *

X = Module(
	identifier="xilinx_csg144",
	description="CSG144 0.8mm BGA for Xilinx XC95144XL, 13x13 balls with center gap"
)

# plastic chip size
D = E = 12.0

# ball array size
W = 13
H = 13

# From https://www.xilinx.com/publications/prod_mktg/pn0010951.pdf
# Suggested footprint:
#   0.35 pad diameter, 0.44 opening in solder mask
# Suggested dimensions for landing via:
#   0.13 (5mil) line width between via and land, 0.56 distance between via and land, 0.51 via, 0.25 hole
# JLCPCB 4-layer minimums: 0.2mm via hole, 0.45mm via, 0.0889 trace/space, 0.127 via-to-trace

# https://www.xilinx.com/support/documentation/user_guides/ug1099-bga-device-design-rules.pdf
# suggests different numbers: 0.4mm pad diameter, 0.43 solder mask opening diameter.

BALL_SPACING = 0.8  # ball pitch.  ball dia is ???
PAD_DIA = 0.35  # diameter of copper pad
MASK_DIA = 0.44  # diameter of opening in solder mask
PAD_CLEARANCE = 0.127  # 5 mil pad clearance, to push it out past the NSMD ring

# top left ball
x0 = -(BALL_SPACING * (W - 1.0) / 2)
y0 = -(BALL_SPACING * (H - 1.0) / 2)

# draw outline
X.add(Line(-D/2, -E/2, -D/2, E/2))
X.add(Line(-D/2, E/2, D/2, E/2))
X.add(Line(D/2, E/2, D/2, -E/2))
X.add(Line(D/2, -E/2, -D/2, -E/2))

# draw pin 1 ID bubble
X.add(Circle(-D/2 + 0.5, -E/2 + 0.5, 0.25))

for y in range(H):
	for x in range(W):
		if x in range(4, 9) and y in range(4, 9):
			continue  # skip center gap
		X.add(Pad(
			name="%s%d" % ("ABCDEFGHJKLMN"[y], x + 1),
			x=x0 + x * BALL_SPACING,
			y=y0 + y * BALL_SPACING,
			w=PAD_DIA,
			h=PAD_DIA,
			shape='circle',
			solder_mask_margin=(MASK_DIA - PAD_DIA) / 2,
			pad_clearance=PAD_CLEARANCE,
		))

X.save()

# Make a version that's able to be routed with 6 mil trace/space

# X.identifier += "_smallpads"
# for elem in X.elements:
# 	if isinstance(elem, Pad):
# 		elem.w = elem.h = 0.342

# X.save()
