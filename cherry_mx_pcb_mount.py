from myelin_kicad_mod import *

# footprint for a single Cherry MX keyswitch (PCB mount version)

X = Module(
	identifier="cherry_mx_pcb_mount",
	description="Cherry MX keyswitch (PCB mount)",
	ref_y = 3.5,
	value_y = 5.5,
)

# bounding boxes (inner/outer)
for box_dia in (13.0, 15.6):
	BOX_HEIGHT = BOX_WIDTH = box_dia

	# draw outline
	X.add(Line(-BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2,  BOX_HEIGHT/2))
	X.add(Line(-BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2,  BOX_HEIGHT/2))
	X.add(Line( BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2, -BOX_HEIGHT/2))
	X.add(Line( BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2, -BOX_HEIGHT/2))

X.add(Pin("M0", 0, 0, 0.157 * INCH))
X.add(Pin("M1", -0.2 * INCH, 0, 0.067 * INCH))
X.add(Pin("M2", 0.2 * INCH, 0, 0.067 * INCH))

X.add(Pin(1, -0.15 * INCH, -0.1 * INCH, 0.059 * INCH + 1, 0.059 * INCH))
X.add(Pin(2, 0.1 * INCH, -0.2 * INCH, 0.059 * INCH + 1, 0.059 * INCH))

X.save()
