from myelin_kicad_mod import *

# Footprint for CUI MD-xxS mini DIN sockets

# Based on measurements from a "D501" jack on Aliexpress, and compared with
# the datasheet for the Pro Signal PSG03463.

for ident, desc, pins in [
    ("minidin_6_ps2_pcb_mount",
     "6-pin mini-DIN for PS/2 keyboard/mouse, CUI MD-60S",
     6),
    ("minidin_9_pcb_mount",
     "9-pin mini-DIN for Acorn mouse, CUI MD-90S",
     9),
]:

    X = Module(
        identifier=ident,
        description=desc,
        ref_y=-5.3,
        value_y=7.3,
    )

    # pad and hole diameters
    HOLE_DIA = 0.9
    RING_DIA = 0.7  # 2 x thickness of plated ring
    PAD_DIA = HOLE_DIA + RING_DIA
    MOUNT_DIA = 1.0

    # bounding box
    BOX_HEIGHT = 12.5
    BOX_WIDTH = 14.0
    BOX_TOP = -BOX_HEIGHT/2
    SHIELD_ROW_Y = BOX_TOP+2.5
    SIGNAL_ROW_1 = BOX_TOP+8.5
    SIGNAL_ROW_2 = BOX_TOP+11.0
    MOUNT_ROW_1 = SIGNAL_ROW_2-9.10+1.50

    # draw outline
    X.add(Line(-BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2,  BOX_HEIGHT/2))
    X.add(Line(-BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2,  BOX_HEIGHT/2))
    X.add(Line( BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2, -BOX_HEIGHT/2))
    X.add(Line( BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2, -BOX_HEIGHT/2))
    # extra line for front
    X.add(Line(-BOX_WIDTH/2, -BOX_HEIGHT/2+1.9, BOX_WIDTH/2, -BOX_HEIGHT/2+1.9))

    # mounting holes
    X.add(Pin("M1", -2.5, MOUNT_ROW_1, MOUNT_DIA, MOUNT_DIA))
    X.add(Pin("M2",  2.5, MOUNT_ROW_1, MOUNT_DIA, MOUNT_DIA))

    # shield pin - shown as a slot in the datasheet, but just a hole here
    X.add(Pin("S1", 0, BOX_TOP+4.7, 2.2+RING_DIA, 2.2))

    # optional shield pins that are on the sockets I have from eBay, and also
    # the CUI MD-xxSM series, but not the MD-xxS
    X.add(Pin("S2", -BOX_WIDTH/2, BOX_TOP+5.5, 2.0+RING_DIA, 2.0))
    X.add(Pin("S3",  BOX_WIDTH/2, BOX_TOP+5.5, 2.0+RING_DIA, 2.0))

    if pins == 6:
        X.add(Pin("M3", -5.0, SIGNAL_ROW_2, MOUNT_DIA, MOUNT_DIA))
        X.add(Pin("M4",  5.0, SIGNAL_ROW_2, MOUNT_DIA, MOUNT_DIA))
        X.add(Pin(1, -1.3, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(2,  1.3, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(3, -3.4, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(4,  3.4, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(5, -3.4, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
        X.add(Pin(6,  3.4, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
    elif pins == 9:
        X.add(Pin("M3", -5.5, SIGNAL_ROW_2, MOUNT_DIA, MOUNT_DIA))
        X.add(Pin("M4",  5.5, SIGNAL_ROW_2, MOUNT_DIA, MOUNT_DIA))
        X.add(Pin(1, -1.3, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(2,  0.7, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(3, -4.0, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(4, -2.0, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
        X.add(Pin(5,    0, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
        X.add(Pin(6,  4.0, SIGNAL_ROW_1, PAD_DIA, HOLE_DIA))
        X.add(Pin(7, -4.0, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
        X.add(Pin(8,  2.0, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
        X.add(Pin(9,  4.0, SIGNAL_ROW_2, PAD_DIA, HOLE_DIA))
    else:
        raise Exception("unknown number of pins %d" % pins)

    X.save()
