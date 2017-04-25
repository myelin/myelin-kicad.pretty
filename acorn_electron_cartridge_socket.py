from myelin_kicad_mod import *

# footprint for AMP-5530843-4 when used as a socket for Acorn Electron cartridges
# 2 rows x 22 pins
# http://www.digikey.com/product-detail/en/5530843-4/A31717-ND/770543?curr=usd&WT.z_cid=ref_octopart_dkc_buynow&site=us
# http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=5530843&DocType=Customer+Drawing&DocLang=English

# C = card slot width = 2.3" = 58.42

X = Module(
	identifier="acorn_electron_cartridge_socket",
	description="AMP-5530843-4 used as Acorn Electron cartridge socket",
	value_x=-14,
	value_y=0,
	ref_x=24,
	ref_y=0,
)

# 44 pins
N = 44

# pad and hole diameters
PAD_DIA = 0.060 * INCH
HOLE_DIA = 0.040 * INCH

# distance between rows
ROW_SEP = 0.191 * INCH
COL_SEP = 0.1 * INCH
WIDTH = (N/2 - 1) * COL_SEP

# bounding box
BOX_HEIGHT = 0.368 * INCH
BOX_WIDTH = 2.460 * INCH

# draw outline
X.add(Line(-BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2,  BOX_HEIGHT/2))
X.add(Line(-BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2,  BOX_HEIGHT/2))
X.add(Line( BOX_WIDTH/2,  BOX_HEIGHT/2,  BOX_WIDTH/2, -BOX_HEIGHT/2))
X.add(Line( BOX_WIDTH/2, -BOX_HEIGHT/2, -BOX_WIDTH/2, -BOX_HEIGHT/2))

# pin A1 and B1 ID text
X.add(Text(BOX_WIDTH/2 + 2, -0.1 * INCH, "A1"))
X.add(Text(BOX_WIDTH/2 + 2, 0.1 * INCH, "B1"))

### rear side: A22 on left, A1 on right
### front side: B22 on left, B1 on right
for pin in range(N/2):
	x = WIDTH / 2 - COL_SEP * pin
	X.add(Pin("A%d" % (pin + 1), x, -ROW_SEP/2, PAD_DIA, HOLE_DIA))
	X.add(Pin("B%d" % (pin + 1), x, ROW_SEP/2, PAD_DIA, HOLE_DIA))

X.save()
