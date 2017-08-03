from myelin_kicad_mod import *

X = Module(
    identifier="bbc_1mhz_bus_board",
    description="Board that fits nicely into the 1MHz bus socket under a BBC Model B",
    ref_x=-17,
    ref_y=15,
    value_x=8,
    value_y=15,
)

# big holes for header pins
PAD_DIA = 0.060 * INCH
HOLE_DIA = 0.040 * INCH

# The dimensions of this board are a kind of terrible.  We have to fit
# everything inside the depth of the 1MHz bus socket (6.5mm / 0.256") plus
# 2.5", i.e. 2.756".  The socket is 0.335" long, and we need to leave about
# 0.3" to make it possible to insert and remove the board from the machine,
# which means we have 2.456" to work with, or 2.121" for the actual board.

# The 1MHz bus socket is 1.9" wide, and we need to provide a notch for the
# locking connector to mate with.  This is around 1/8" long, and is
# approximately 5/16-7/16 out from the case.

# origin is in the center of the back wall of the socket in the bbc micro,
# i.e. 6.5mm inside the machine.

BOARD_WIDTH = 1.9 * INCH
BOARD_HEIGHT = 2.1 * INCH
CHAMFER = 1

# the holes in the plug are 6.5mm deep, which fairly closely matches
# the distance from the case edge to the base of the pins
BBC_CASE_EDGE_Y = 6.5

# the female plug is 8.5mm long, so this is where our board starts
BOARD_TOP_EDGE_Y = 8.5
BOARD_BOTTOM_EDGE_Y = BOARD_TOP_EDGE_Y + BOARD_HEIGHT

# 1.6mm from the end of the female plug to the first row of pins
FIRST_ROW_OF_PINS_Y = BOARD_TOP_EDGE_Y + 1.6

# line representing the back of the connector
X.add(Line(-BOARD_WIDTH/2, 0, BOARD_WIDTH/2, 0))

# line representing the edge of the computer's case
X.add(Line(-BOARD_WIDTH/2, BBC_CASE_EDGE_Y, BOARD_WIDTH/2, BBC_CASE_EDGE_Y))

# board outline
# - top
X.add(Line(-BOARD_WIDTH/2 + CHAMFER, BOARD_TOP_EDGE_Y,
            BOARD_WIDTH/2 - CHAMFER, BOARD_TOP_EDGE_Y, layers=EDGE))
# - top left corner
X.add(Line(-BOARD_WIDTH/2 + CHAMFER, BOARD_TOP_EDGE_Y,
           -BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER, layers=EDGE))
# - left
X.add(Line(-BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER,
           -BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER, layers=EDGE))
# - bottom left corner
X.add(Line(-BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER,
           -BOARD_WIDTH/2 + CHAMFER, BOARD_BOTTOM_EDGE_Y, layers=EDGE))
# - bottom
X.add(Line(-BOARD_WIDTH/2 + CHAMFER, BOARD_BOTTOM_EDGE_Y,
            BOARD_WIDTH/2 - CHAMFER, BOARD_BOTTOM_EDGE_Y, layers=EDGE))
# - bottom right corner
X.add(Line( BOARD_WIDTH/2 - CHAMFER, BOARD_BOTTOM_EDGE_Y,
            BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER, layers=EDGE))
# - right
X.add(Line( BOARD_WIDTH/2, BOARD_BOTTOM_EDGE_Y - CHAMFER,
            BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER, layers=EDGE))
# - top right corner
X.add(Line( BOARD_WIDTH/2 - CHAMFER, BOARD_TOP_EDGE_Y,
            BOARD_WIDTH/2, BOARD_TOP_EDGE_Y + CHAMFER, layers=EDGE))

PINS_X = 17 # cols
PINS_Y = 2 # rows
SPACING = 2.54

# pin 1 is on the far left, bottom row
PIN1_X = -(float(PINS_X - 1) / 2 * SPACING)
PIN1_Y = FIRST_ROW_OF_PINS_Y + SPACING

for pin_x in range(PINS_X):
    for pin_y in range(PINS_Y):
        X.add(Pin(
            name=str(pin_x * PINS_Y + pin_y + 1),
            x=PIN1_X + SPACING * pin_x,
            y=PIN1_Y - SPACING * pin_y,
            dia=PAD_DIA,
            hole_dia=HOLE_DIA,
            square=(pin_x == 0 and pin_y == 0)
        ))

X.save()
