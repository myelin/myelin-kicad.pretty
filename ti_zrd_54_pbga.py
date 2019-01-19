from myelin_kicad_mod import *

X = Module(
    identifier="ti_zrd_54_pbga",
    description="TI R-PBGA-N54 ZRD 54-ball 0.8mm BGA for buffers"
    # http://www.ti.com/lit/ml/mpbg320a/mpbg320a.pdf
)

# References:

# https://macrofab.com/blog/escaping-bgas-methods-routing-traces-bga-footprints/
# -> pads typ 20% smaller than ball dia, i.e. .48

# I don't see any suggested numbers in the TI documentation, so I'm going to
# use 0.4mm pads and 0.43mm solder mask openings, as suggested in Xilinx's
# UG1099 for NSMD soldering of 0.8mm BGA.  I think this should work OK for
# 0.5mm balls.

# plastic chip X/Y size
D = 5.5
E = 8

# ball array size
W = 6
H = 9

BALL_SPACING = 0.8  # ball pitch.  ball dia is 0.5mm.
PAD_DIA = 0.4  # diameter of copper pad
MASK_DIA = 0.43  # diameter of opening in solder mask
PAD_CLEARANCE = 0.127  # 5 mil clearance from pad to track

# top left ball
x0 = -(BALL_SPACING * (W - 1.0) / 2)
y0 = -(BALL_SPACING * (H - 1.0) / 2)

# draw outline
X.add(Line(-D/2, -E/2, -D/2, E/2))
X.add(Line(-D/2, E/2, D/2, E/2))
X.add(Line(D/2, E/2, D/2, -E/2))
X.add(Line(D/2, -E/2, -D/2, -E/2))

# draw pin 1 ID
X.add(Line(-D/2-0.5, -E/2-0.5, -D/2-0.5, -E/2+1.5))
X.add(Line(-D/2-0.5, -E/2-0.5, -D/2+1.5, -E/2-0.5))

for y in range(H):
    for x in range(W):
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
