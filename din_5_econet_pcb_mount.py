from myelin_kicad_mod import *

# Footprint for the 5-pin DIN socket used for the BBC Model B's Econet port

# Based on measurements from a "D501" jack on Aliexpress, and compared with
# the datasheet for the Pro Signal PSG03463.

X = Module(
	identifier="din_5_econet_pcb_mount",
	description="5-pin Econet socket to match footprint on the BBC Model B",
    value_y=2.54,
)

# pad and hole diameters
HOLE_DIA = 1.5
PAD_DIA = HOLE_DIA + 0.75

# bounding box
BOX_HEIGHT = 14.5  # PSG is 19.0
BOX_WIDTH = 19.7  # PSG is 21.0
BOX_TOP = -BOX_HEIGHT/2
SHIELD_ROW_Y = BOX_TOP+2.5
SIGNAL_ROW_1 = BOX_TOP+12.3  # PSG is 12.5
SIGNAL_ROW_2 = BOX_TOP+14.5  # PSG is 15.0
PIN_1_3_X = 14.7/2  # PSG is
PIN_4_5_X = 10.0/2

# draw outline
X.add(Line(-BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2,  BOX_HEIGHT/2))
X.add(Line(-BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2,  BOX_HEIGHT/2))
X.add(Line( BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2, -BOX_HEIGHT/2))
X.add(Line( BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2, -BOX_HEIGHT/2))

# shield pins are 2.5mm below top
X.add(Pin("S1", -5.0, BOX_TOP+2.5, PAD_DIA, HOLE_DIA))
X.add(Pin("S2", -2.5, BOX_TOP+2.5, PAD_DIA, HOLE_DIA))
X.add(Pin("S3", 2.5, BOX_TOP+2.5, PAD_DIA, HOLE_DIA))
X.add(Pin("S4", 5.0, BOX_TOP+2.5, PAD_DIA, HOLE_DIA))

# some sockets have extra pins here
X.add(Pin("M1", -15.01/2, BOX_TOP+7.5, 2.39, 2.39))
X.add(Pin("M2", 15.01/2, BOX_TOP+7.5, 2.39, 2.39))

# signal pins are 12.5 and 15 below top
X.add(Pin(2, 0, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
X.add(Pin(1, -PIN_1_3_X, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
X.add(Pin(3, PIN_1_3_X, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
X.add(Pin(4, -PIN_4_5_X, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
X.add(Pin(5, PIN_4_5_X, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))

X.save()
