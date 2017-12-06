from myelin_kicad_mod import *

X = Module(
    identifier="lcsoft_mini_flipped",
    description="lcsoft mini logic analyzer, installed face-down",
    ref_x=0,
    ref_y=-2,
    value_x=0,
    value_y=2,
)

# big holes for header pins
PAD_DIA = 0.060 * INCH
HOLE_DIA = 0.040 * INCH

BOARD_WIDTH = 1.6 * INCH
BOARD_HEIGHT = 56.5
BOARD_TOP_EDGE_Y = -BOARD_HEIGHT/2
BOARD_BOTTOM_EDGE_Y = BOARD_TOP_EDGE_Y + BOARD_HEIGHT
CHAMFER = 1.0

X.add(Line(-BOARD_WIDTH/2 + CHAMFER, BOARD_TOP_EDGE_Y,
            BOARD_WIDTH/2 - CHAMFER, BOARD_TOP_EDGE_Y, layers=[FRONT_SILK]))
# - top left corner
X.add(Line(-BOARD_WIDTH/2 + CHAMFER, BOARD_TOP_EDGE_Y,
           -BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER, layers=[FRONT_SILK]))
# - left
X.add(Line(-BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER,
           -BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER, layers=[FRONT_SILK]))
# - bottom left corner
X.add(Line(-BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER,
           -BOARD_WIDTH/2 + CHAMFER, BOARD_BOTTOM_EDGE_Y, layers=[FRONT_SILK]))
# - bottom
X.add(Line(-BOARD_WIDTH/2 + CHAMFER, BOARD_BOTTOM_EDGE_Y,
            BOARD_WIDTH/2 - CHAMFER, BOARD_BOTTOM_EDGE_Y, layers=[FRONT_SILK]))
# - bottom right corner
X.add(Line( BOARD_WIDTH/2 - CHAMFER, BOARD_BOTTOM_EDGE_Y,
            BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER, layers=[FRONT_SILK]))
# - right
X.add(Line( BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER,
            BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER, layers=[FRONT_SILK]))
# - top right corner
X.add(Line( BOARD_WIDTH/2 - CHAMFER, BOARD_TOP_EDGE_Y,
            BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER, layers=[FRONT_SILK]))

start_y = -5 * 2.54 + 0.2 * INCH  # slightly below center
row_sep = 1.1 * 25.4
start_x = -(row_sep + 2.54) / 2
for side, x_offset in (("L", 0), ("R", row_sep)):
    for col in (0, 1):
        for row in range(10):
            pin_id = "%s%d" % (side, row * 2 + col + 1)
            X.add(Pin(
                name = pin_id,
                x = -(start_x + x_offset + col * 2.54),
                y = start_y + row * 2.54,
                dia = PAD_DIA,
                hole_dia = HOLE_DIA,
                square = (col == 0 and row == 0),
            ))

X.save()
