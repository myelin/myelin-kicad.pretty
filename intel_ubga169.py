from myelin_kicad_mod import *

X = Module(
	identifier="intel_ubga169",
	description="UBGA169 for Intel Max 10 FPGAs"
)

# Intel recommends 0.34mm NSMD pads for 0.8mm UBGA chips:
# https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/an/an114.pdf

# plastic chip is 11 mm x 11 mm
D = E = 11.0

W = 13
H = 13

# 0.8mm ball spacing, 0.5mm ball dia, 0.4mm pad dia
BALL_SPACING = 0.8  # ball pitch.  ball dia is 0.5
PAD_DIA = 0.34  # diameter of copper pad
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

"""
10M08SCU169 pinout:

Bank Number	VREF	Pin Name/Function	Optional Function(s)	Configuration Function	Dedicated Tx/Rx Channel	Emulated LVDS Output Channel	IO Performance	U169
"""

description_lines = """
1A	VREFB1N0	IO			DIFFIO_RX_L1n	DIFFOUT_L1n	Low_Speed	D1
1A	VREFB1N0	IO			DIFFIO_RX_L1p	DIFFOUT_L1p	Low_Speed	C2
1A	VREFB1N0	IO			DIFFIO_RX_L3n	DIFFOUT_L3n	Low_Speed	E3
1A	VREFB1N0	IO			DIFFIO_RX_L3p	DIFFOUT_L3p	Low_Speed	E4
1A	VREFB1N0	IO			DIFFIO_RX_L5n	DIFFOUT_L5n	Low_Speed	C1
1A	VREFB1N0	IO			DIFFIO_RX_L5p	DIFFOUT_L5p	Low_Speed	B1
1A	VREFB1N0	IO			DIFFIO_RX_L7n	DIFFOUT_L7n	Low_Speed	F1
1A	VREFB1N0	IO			DIFFIO_RX_L7p	DIFFOUT_L7p	Low_Speed	E1
1B	VREFB1N0	IO		JTAGEN				E5
1B	VREFB1N0	IO		TMS	DIFFIO_RX_L11n	DIFFOUT_L11n	Low_Speed	G1
1B	VREFB1N0	IO	VREFB1N0					H1
1B	VREFB1N0	IO		TCK	DIFFIO_RX_L11p	DIFFOUT_L11p	Low_Speed	G2
1B	VREFB1N0	IO		TDI	DIFFIO_RX_L12n	DIFFOUT_L12n	Low_Speed	F5
1B	VREFB1N0	IO		TDO	DIFFIO_RX_L12p	DIFFOUT_L12p	Low_Speed	F6
1B	VREFB1N0	IO			DIFFIO_RX_L14n	DIFFOUT_L14n	Low_Speed	F4
1B	VREFB1N0	IO			DIFFIO_RX_L14p	DIFFOUT_L14p	Low_Speed	G4
1B	VREFB1N0	IO			DIFFIO_RX_L16n	DIFFOUT_L16n	Low_Speed	H2
1B	VREFB1N0	IO			DIFFIO_RX_L16p	DIFFOUT_L16p	Low_Speed	H3

2	VREFB2N0	IO	CLK0n		DIFFIO_RX_L18n	DIFFOUT_L18n	High_Speed	G5
2	VREFB2N0	IO			DIFFIO_RX_L19n	DIFFOUT_L19n	High_Speed	J1
2	VREFB2N0	IO	CLK0p		DIFFIO_RX_L18p	DIFFOUT_L18p	High_Speed	H6
2	VREFB2N0	IO			DIFFIO_RX_L19p	DIFFOUT_L19p	High_Speed	J2
2	VREFB2N0	IO	CLK1n		DIFFIO_RX_L20n	DIFFOUT_L20n	High_Speed	H5
2	VREFB2N0	IO			DIFFIO_RX_L21n	DIFFOUT_L21n	High_Speed	M1
2	VREFB2N0	IO	CLK1p		DIFFIO_RX_L20p	DIFFOUT_L20p	High_Speed	H4
2	VREFB2N0	IO			DIFFIO_RX_L21p	DIFFOUT_L21p	High_Speed	M2
2	VREFB2N0	IO	DPCLK0		DIFFIO_RX_L22n	DIFFOUT_L22n	High_Speed	N2
2	VREFB2N0	IO	VREFB2N0					L1
2	VREFB2N0	IO	DPCLK1		DIFFIO_RX_L22p	DIFFOUT_L22p	High_Speed	N3
2	VREFB2N0	IO						L2
2	VREFB2N0	IO	PLL_L_CLKOUTn		DIFFIO_RX_L27n	DIFFOUT_L27n	High_Speed	M3
2	VREFB2N0	IO			DIFFIO_RX_L28n	DIFFOUT_L28n	High_Speed	K1
2	VREFB2N0	IO	PLL_L_CLKOUTp		DIFFIO_RX_L27p	DIFFOUT_L27p	High_Speed	L3
2	VREFB2N0	IO			DIFFIO_RX_L28p	DIFFOUT_L28p	High_Speed	K2

3	VREFB3N0	IO			DIFFIO_TX_RX_B1n	DIFFOUT_B1n	High_Speed	L5
3	VREFB3N0	IO			DIFFIO_RX_B2n	DIFFOUT_B2n	High_Speed	M4
3	VREFB3N0	IO			DIFFIO_TX_RX_B1p	DIFFOUT_B1p	High_Speed	L4
3	VREFB3N0	IO			DIFFIO_RX_B2p	DIFFOUT_B2p	High_Speed	M5
3	VREFB3N0	IO			DIFFIO_TX_RX_B3n	DIFFOUT_B3n	High_Speed	K5
3	VREFB3N0	IO			DIFFIO_RX_B4n	DIFFOUT_B4n	High_Speed	N4
3	VREFB3N0	IO			DIFFIO_TX_RX_B3p	DIFFOUT_B3p	High_Speed	J5
3	VREFB3N0	IO			DIFFIO_RX_B4p	DIFFOUT_B4p	High_Speed	N5
3	VREFB3N0	IO			DIFFIO_TX_RX_B5n	DIFFOUT_B5n	High_Speed	N6
3	VREFB3N0	IO			DIFFIO_RX_B6n	DIFFOUT_B6n	High_Speed	N7
3	VREFB3N0	IO			DIFFIO_TX_RX_B5p	DIFFOUT_B5p	High_Speed	M7
3	VREFB3N0	IO			DIFFIO_RX_B6p	DIFFOUT_B6p	High_Speed	N8
3	VREFB3N0	IO			DIFFIO_TX_RX_B7n	DIFFOUT_B7n	High_Speed	J6
3	VREFB3N0	IO			DIFFIO_RX_B8n	DIFFOUT_B8n	High_Speed	M8
3	VREFB3N0	IO			DIFFIO_TX_RX_B7p	DIFFOUT_B7p	High_Speed	K6
3	VREFB3N0	IO			DIFFIO_RX_B8p	DIFFOUT_B8p	High_Speed	M9
3	VREFB3N0	IO			DIFFIO_TX_RX_B9n	DIFFOUT_B9n	High_Speed	J7
3	VREFB3N0	IO	VREFB3N0					N11
3	VREFB3N0	IO			DIFFIO_TX_RX_B9p	DIFFOUT_B9p	High_Speed	K7
3	VREFB3N0	IO						N12
3	VREFB3N0	IO			DIFFIO_TX_RX_B10n	DIFFOUT_B10n	High_Speed	M13
3	VREFB3N0	IO			DIFFIO_RX_B11n	DIFFOUT_B11n	High_Speed	N10
3	VREFB3N0	IO			DIFFIO_TX_RX_B10p	DIFFOUT_B10p	High_Speed	M12
3	VREFB3N0	IO			DIFFIO_RX_B11p	DIFFOUT_B11p	High_Speed	N9
3	VREFB3N0	IO			DIFFIO_TX_RX_B12n	DIFFOUT_B12n	High_Speed	M11
3	VREFB3N0	IO			DIFFIO_TX_RX_B12p	DIFFOUT_B12p	High_Speed	L11
3	VREFB3N0	IO			DIFFIO_TX_RX_B14n	DIFFOUT_B14n	High_Speed	J8
3	VREFB3N0	IO			DIFFIO_TX_RX_B14p	DIFFOUT_B14p	High_Speed	K8
3	VREFB3N0	IO			DIFFIO_TX_RX_B16n	DIFFOUT_B16n	High_Speed	M10
3	VREFB3N0	IO			DIFFIO_TX_RX_B16p	DIFFOUT_B16p	High_Speed	L10
5	VREFB5N0	IO			DIFFIO_RX_R1p	DIFFOUT_R1p	High_Speed	K10
5	VREFB5N0	IO			DIFFIO_RX_R2p	DIFFOUT_R2p	High_Speed	K11
5	VREFB5N0	IO			DIFFIO_RX_R1n	DIFFOUT_R1n	High_Speed	J10
5	VREFB5N0	IO			DIFFIO_RX_R2n	DIFFOUT_R2n	High_Speed	L12
5	VREFB5N0	IO			DIFFIO_RX_R7p	DIFFOUT_R7p	High_Speed	K12
5	VREFB5N0	IO						L13
5	VREFB5N0	IO			DIFFIO_RX_R7n	DIFFOUT_R7n	High_Speed	J12
5	VREFB5N0	IO	VREFB5N0					K13
5	VREFB5N0	IO			DIFFIO_RX_R8p	DIFFOUT_R8p	High_Speed	J9
5	VREFB5N0	IO			DIFFIO_RX_R9p	DIFFOUT_R9p	High_Speed	J13
5	VREFB5N0	IO			DIFFIO_RX_R8n	DIFFOUT_R8n	High_Speed	H10
5	VREFB5N0	IO			DIFFIO_RX_R9n	DIFFOUT_R9n	High_Speed	H13
5	VREFB5N0	IO			DIFFIO_RX_R10p	DIFFOUT_R10p	High_Speed	H9
5	VREFB5N0	IO			DIFFIO_RX_R11p	DIFFOUT_R11p	High_Speed	G13
5	VREFB5N0	IO			DIFFIO_RX_R10n	DIFFOUT_R10n	High_Speed	H8
5	VREFB5N0	IO			DIFFIO_RX_R11n	DIFFOUT_R11n	High_Speed	G12
6	VREFB6N0	IO	CLK2p		DIFFIO_RX_R14p	DIFFOUT_R14p	High_Speed	G9
6	VREFB6N0	IO	CLK2n		DIFFIO_RX_R14n	DIFFOUT_R14n	High_Speed	G10
6	VREFB6N0	IO	CLK3p		DIFFIO_RX_R16p	DIFFOUT_R16p	High_Speed	F13
6	VREFB6N0	IO	CLK3n		DIFFIO_RX_R16n	DIFFOUT_R16n	High_Speed	E13
6	VREFB6N0	IO			DIFFIO_RX_R18p	DIFFOUT_R18p	High_Speed	F12
6	VREFB6N0	IO			DIFFIO_RX_R18n	DIFFOUT_R18n	High_Speed	E12
6	VREFB6N0	IO	DPCLK3		DIFFIO_RX_R26p	DIFFOUT_R26p	High_Speed	F9
6	VREFB6N0	IO	VREFB6N0					D13
6	VREFB6N0	IO	DPCLK2		DIFFIO_RX_R26n	DIFFOUT_R26n	High_Speed	F10
6	VREFB6N0	IO						C13
6	VREFB6N0	IO			DIFFIO_RX_R27p	DIFFOUT_R27p	High_Speed	F8
6	VREFB6N0	IO			DIFFIO_RX_R28p	DIFFOUT_R28p	High_Speed	B12
6	VREFB6N0	IO			DIFFIO_RX_R27n	DIFFOUT_R27n	High_Speed	E9
6	VREFB6N0	IO			DIFFIO_RX_R28n	DIFFOUT_R28n	High_Speed	B11
6	VREFB6N0	IO			DIFFIO_RX_R29p	DIFFOUT_R29p	High_Speed	C12
6	VREFB6N0	IO			DIFFIO_RX_R30p	DIFFOUT_R30p	High_Speed	B13
6	VREFB6N0	IO			DIFFIO_RX_R29n	DIFFOUT_R29n	High_Speed	C11
6	VREFB6N0	IO			DIFFIO_RX_R30n	DIFFOUT_R30n	High_Speed	A12
6	VREFB6N0	IO			DIFFIO_RX_R31p	DIFFOUT_R31p	High_Speed	E10
6	VREFB6N0	IO			DIFFIO_RX_R31n	DIFFOUT_R31n	High_Speed	D9
6	VREFB6N0	IO			DIFFIO_RX_R33p	DIFFOUT_R33p	High_Speed	D12
6	VREFB6N0	IO			DIFFIO_RX_R33n	DIFFOUT_R33n	High_Speed	D11

8	VREFB8N0	IO			DIFFIO_RX_T14p	DIFFOUT_T14p	Low_Speed	C10
8	VREFB8N0	IO			DIFFIO_RX_T15p	DIFFOUT_T15p	Low_Speed	A8
8	VREFB8N0	IO			DIFFIO_RX_T14n	DIFFOUT_T14n	Low_Speed	C9
8	VREFB8N0	IO			DIFFIO_RX_T15n	DIFFOUT_T15n	Low_Speed	A9
8	VREFB8N0	IO			DIFFIO_RX_T16p	DIFFOUT_T16p	Low_Speed	B10
8	VREFB8N0	IO			DIFFIO_RX_T17p	DIFFOUT_T17p	Low_Speed	A10
8	VREFB8N0	IO		DEV_CLRn	DIFFIO_RX_T16n	DIFFOUT_T16n	Low_Speed	B9
8	VREFB8N0	IO			DIFFIO_RX_T17n	DIFFOUT_T17n	Low_Speed	A11
8	VREFB8N0	IO		DEV_OE	DIFFIO_RX_T18p	DIFFOUT_T18p	Low_Speed	D8
8	VREFB8N0	IO			DIFFIO_RX_T18n	DIFFOUT_T18n	Low_Speed	E8
8	VREFB8N0	IO	VREFB8N0					B7
8	VREFB8N0	IO		CONFIG_SEL				D7
8	VREFB8N0	IO			DIFFIO_RX_T19p	DIFFOUT_T19p	Low_Speed	A7
8	VREFB8N0	Input_only		nCONFIG				E7
8	VREFB8N0	IO			DIFFIO_RX_T19n	DIFFOUT_T19n	Low_Speed	A6
8	VREFB8N0	IO			DIFFIO_RX_T20p	DIFFOUT_T20p	Low_Speed	B6
8	VREFB8N0	IO			DIFFIO_RX_T21p	DIFFOUT_T21p	Low_Speed	A4
8	VREFB8N0	IO			DIFFIO_RX_T20n	DIFFOUT_T20n	Low_Speed	B5
8	VREFB8N0	IO			DIFFIO_RX_T21n	DIFFOUT_T21n	Low_Speed	A3
8	VREFB8N0	IO			DIFFIO_RX_T22p	DIFFOUT_T22p	Low_Speed	E6
8	VREFB8N0	IO			DIFFIO_RX_T23p	DIFFOUT_T23p	Low_Speed	B3
8	VREFB8N0	IO		CRC_ERROR	DIFFIO_RX_T22n	DIFFOUT_T22n	Low_Speed	D6
8	VREFB8N0	IO			DIFFIO_RX_T23n	DIFFOUT_T23n	Low_Speed	B4
8	VREFB8N0	IO		nSTATUS	DIFFIO_RX_T24p	DIFFOUT_T24p	Low_Speed	C4
8	VREFB8N0	IO						A5
8	VREFB8N0	IO		CONF_DONE	DIFFIO_RX_T24n	DIFFOUT_T24n	Low_Speed	C5
8	VREFB8N0	IO			DIFFIO_RX_T26p	DIFFOUT_T26p	Low_Speed	A2
8	VREFB8N0	IO			DIFFIO_RX_T26n	DIFFOUT_T26n	Low_Speed	B2
		GND						D2
		GND						E2
		GND						N13
		GND						N1
		GND						M6
		GND						L9
		GND						J4
		GND						H12
		GND						G7
		GND						F3
		GND						E11
		GND						D5
		GND						C3
		GND						B8
		GND						A13
		GND						A1
		VCCIO1A						F2
		VCCIO1B						G3
		VCCIO2						K3
		VCCIO2						J3
		VCCIO3						L8
		VCCIO3						L7
		VCCIO3						L6
		VCCIO5						J11
		VCCIO5						H11
		VCCIO6						G11
		VCCIO6						F11
		VCCIO8						C8
		VCCIO8						C7
		VCCIO8						C6
		VCCA1						K4
		VCCA2						D10
		VCCA3						D3
		VCCA3						D4
		VCCA4						K9
		VCC_ONE						H7
		VCC_ONE						G8
		VCC_ONE						G6
		VCC_ONE						F7
""".split("\n")

iocount = 0
confcount = 0
for line in description_lines:
	if not line.strip(): continue
	bits = line.split("\t")
	bank, vref, elec, special, config, diffio, diffout, speed, pin = bits
	#print bank, vref, elec, special, q, diffio, diffout, speed, pin
	print pin,
	if config:
		print "config: %s" % config
		confcount += 1
		pin_io_id = "fpga_%s" % config
	elif elec != "IO":
		print "not IO: %s" % elec
		if elec.startswith("VCC"):
			pin_io_id = "3V3" 
		elif elec == "GND":
			pin_io_id = "GND"
		else:
			raise Exception("bad elec for %s: %s" % (pin, elec))
	else:
		if diffio:
			diffio_id = diffio.split("_")[-1]
			if special:
				pin_io_id = "special_b%s_%s_%s_%s" % (bank, special, diffio_id, pin)
			else:
				pin_io_id = "io_b%s_%s_%s" % (bank, diffio_id, pin)
		elif special:
			pin_io_id = "special_%s_nodiff_%s" % (vref, pin)
		else:
			pin_io_id = "TODO_unknown_b%s_%s" % (bank, pin)

		print "normal: bank=%s elec=%s special=%s diffio=%s diffout=%s speed=%s pin=%s io_id=%s" % (
			bank, elec, special, diffio, diffout, speed, pin, pin_io_id)
		iocount += 1

	print('Pin("%s", "", "%s"),' % (pin, pin_io_id))
print "%d ios + %d config" % (iocount, confcount)

