from myelin_kicad_mod import *

# Datasheet: http://www.mouser.com/ds/2/18/UE27ACX4X0X-45641.pdf
X = Module(
    identifier="usb_a_host_pth_amphenol",
    description="Amphenol UE27AC54100 USB A socket for USB hosts",
    ref_x=0,
    ref_y=7,
    value_x=0,
    value_y=8.5,
)


# Origin: x = center of socket, y = top of socket.

OUTLINE_WIDTH = 13.1  # excluding tabs and flanges
OUTLINE_LEFT = -OUTLINE_WIDTH/2
OUTLINE_RIGHT = OUTLINE_WIDTH/2
OUTLINE_TOP = 0
OUTLINE_BOTTOM = OUTLINE_TOP + 13.85  # including flanges, so this should be slightly off the PCB
X.add(Text(0, OUTLINE_BOTTOM - 1, "board edge"))

# two mounting holes, 13.14 mm apart
MOUNTING_HOLES_Y = OUTLINE_BOTTOM - 10.28
MOUNTING_HOLES_X = [
	-13.14/2,
	13.14/2,
]
MOUNTING_HOLE_DIA = 2.3
# four pins, with 2.5/2/2.5 separation
PINS_Y = MOUNTING_HOLES_Y - 2.71
PINS_X = [
	-1 - 2.5,
	-1,
	1,
	1 + 2.5,
]
PIN_HOLE_DIA = 0.92
PIN_PAD_DIA = PIN_HOLE_DIA + 0.8

# outline of socket (including flanges -- TODO figure out where the edge of the PCB goes)
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_TOP))
X.add(Line(OUTLINE_LEFT, OUTLINE_TOP, OUTLINE_LEFT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_LEFT, OUTLINE_BOTTOM, OUTLINE_RIGHT, OUTLINE_BOTTOM))
X.add(Line(OUTLINE_RIGHT, OUTLINE_TOP, OUTLINE_RIGHT, OUTLINE_BOTTOM))

# mounting holes
for hole_idx in range(len(MOUNTING_HOLES_X)):
	X.add(Pin("H%d" % (hole_idx + 1), MOUNTING_HOLES_X[hole_idx], MOUNTING_HOLES_Y, MOUNTING_HOLE_DIA, MOUNTING_HOLE_DIA))

# pins
for pin_idx in range(len(PINS_X)):
	X.add(Pin(pin_idx + 1, PINS_X[pin_idx], PINS_Y, PIN_PAD_DIA, PIN_HOLE_DIA))

X.save()
