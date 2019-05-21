from myelin_kicad_mod import *

# References:

# http://www.cypress.com/file/45826/download
# AN79938 Design Guidelines for Cypress Ball Grid Array (BGA) Packaged Devices 

# http://www.cypress.com/file/202451/download
# AN202751 Surface Mount Assembly Recommendations for Cypress FBGA Packages

# http://www.cypress.com/file/202531/download
# AN99178 Solder Mask and Trace Recommendations for FBGAs

# Cypress recommends NSMD pads; for 1.00mm ball spacing that means:
# NSMD pad 0.45mm, mask 0.60mm
# SMD pad 0.6mm, mask 0.0.5mm

# https://macrofab.com/blog/escaping-bgas-methods-routing-traces-bga-footprints/
# -> pads typ 20% smaller than ball dia, i.e. .48

for version in ("", "_smallpads"):

    X = Module(
        identifier="lattice_ftg256_fbga%s" % version,
        description="ftg256 256-ball 1.0mm BGA for Lattice MachXO2 FPGA"
    )

    # plastic chip size
    D = E = 17.0

    # ball array size
    W = 16
    H = 16

    # Values from https://www.xilinx.com/support/documentation/user_guides/ug1099-bga-device-design-rules.pdf
    # Solder mask opening slightly wider than pad, for NSMD.
    # 13+ mil gap between clearance rings (23 mil between rings) to allow two 4mil traces with 5mil spacing through.
    # 39.37 - 23 = 16.37 mil for mask opening, i.e. .4158.
    BALL_SPACING = 1.0  # ball pitch.  ball dia is 0.6mm.
    if version == '_smallpads':
        # non-recommended version that will make routing easier for two layer
        # boards.
        PAD_DIA = 0.35
    else:
        # recommended by Lattice TN1074 for MachXO2 ftBGA
        PAD_DIA = 0.4  # diameter of copper pad
    MASK_DIA = PAD_DIA + 0.05  # diameter of opening in solder mask
    PAD_CLEARANCE = 0  # Just use default clearance

    # top left ball
    x0 = -(BALL_SPACING * (W - 1.0) / 2)
    y0 = -(BALL_SPACING * (H - 1.0) / 2)

    # draw outline
    X.add(Line(-D/2, -E/2, -D/2, E/2))
    X.add(Line(-D/2, E/2, D/2, E/2))
    X.add(Line(D/2, E/2, D/2, -E/2))
    X.add(Line(D/2, -E/2, -D/2, -E/2))

    # draw pin 1 ID bubble and chevron
    X.add(Circle(-D/2 + 0.5, -E/2 + 0.5, 0.25))
    X.add(Line(-D/2-0.5, -E/2-0.5, -D/2+1, -E/2-0.5))
    X.add(Line(-D/2-0.5, -E/2-0.5, -D/2-0.5, -E/2+1))

    for y in range(H):
        for x in range(W):
            X.add(Pad(
                name="%s%d" % ("ABCDEFGHJKLMNPRT"[y], x + 1),
                x=x0 + x * BALL_SPACING,
                y=y0 + y * BALL_SPACING,
                w=PAD_DIA,
                h=PAD_DIA,
                shape='circle',
                solder_mask_margin=(MASK_DIA - PAD_DIA) / 2,
                pad_clearance=PAD_CLEARANCE,
            ))


    X.save()
