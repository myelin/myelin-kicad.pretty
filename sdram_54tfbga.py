from myelin_kicad_mod import *

X = Module(
	identifier="sdram_54tfbga",
	description="54 ball TFBGA for SDRAM chips"
)

# e.g. https://www.alliancememory.com/wp-content/uploads/pdf/dram/256Mb-AS4C16M16SA-C&I_V3.0_March%202015.pdf

# plastic chip dimensions
D = E = 8.0

W = 9  # with 3 empty rows in the middle
H = 9

# 0.8mm ball spacing, 0.45mm ball dia
BALL_SPACING = 0.8  # ball pitch
PAD_DIA = 0.36  # diameter of copper pad (80% of ball); could prob go as low as 0.32
MASK_DIA = PAD_DIA + 0.03  # diameter of opening in solder mask
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
		if x in (3, 4, 5): continue
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
