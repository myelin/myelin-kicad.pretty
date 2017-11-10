# 100-pin MachXO2-640 or -1200 chip
# 78 GPIOs or 39 differential I/O
# 8 VCCIO, 2 VCC, 8 GND, 3 NC, 4 jtag, 4-5 random config pins
# That leaves 70 actual GPIOs

# Lattice says:
# Pull up PROGRAMN (to avoid accidental entry into programming mode)
# Pull up INITN (in programming doc but not hw checklist)
# Pull up DONE
# Pull up SN (to avoid going into SPI slave mode)
# Pull up CSSPIN in case we want to use external or dual boot config mode
# Pull up TCK with 4.7k

# The eval board pulls TDI, TDO, TMS up with 5k1, TCK down with 2k2, SDA and SCL up with 2k2,
# and nothing obvious on PROGRAMN, INITN, DONE, SN, or CSSPIN.

# A forum entry says all you need is the pullup or pulldown on TCK.

# Connects to:
# - CPU A0-15, D0-7, RnW, PHI0, 16MHZ (maybe), IRQ, NMI = 29 pins (41 left)


fpga = Component(
    footprint="",
    identifier="U?",
    value="LCMXO2-640HC-4TG100", # -4, -5, -6?  difference?
    pins=[
        Pin(1, "", [""]), # 1200: L_GPLLT_IN
        Pin(2, "", [""]), # 1200: L_GPLLC_IN
        Pin(3, "", [""]), # PCLKT3_2
        Pin(4, "", [""]), # PCLKC3_2
        Pin(5, "VCCIO3", ["3V3"]),
        Pin(6, "GND", ["GND"]),
        Pin(7, "", [""]),
        Pin(8, "", [""]),
        Pin(9, "", [""]),
        Pin(10, "", [""]),
        Pin(11, "NC"),
        Pin(12, "", [""]), # PCLKT3_1
        Pin(13, "", [""]), # PCLKC3_1
        Pin(14, "", [""]),
        Pin(15, "", [""]),
        Pin(16, "", [""]),
        Pin(17, "", [""]),
        Pin(18, "", [""]),
        Pin(19, "", [""]),
        Pin(20, "", [""]), # PCLKT3_0
        Pin(21, "", [""]), # PCLKC3_0
        Pin(22, "GND", ["GND"]),
        Pin(23, "VCCIO3", ["3V3"]),
        Pin(24, "", [""]),
        Pin(25, "", [""]),
        Pin(26, "VCCIO2", ["3V3"]),
        Pin(27, "CSSPIN", [""]),
        Pin(28, "", [""]),
        Pin(29, "", [""]),
        Pin(30, "", [""]),
        Pin(31, "MCLK/CCLK", [""]),
        Pin(32, "SO/SPISO", [""]),
        Pin(33, "GND", ["GND"]),
        Pin(34, "", [""]), # PCLKT2_0
        Pin(35, "", [""]), # PCLKC2_0
        Pin(36, "", [""]),
        Pin(37, "", [""]),
        Pin(38, "", [""]), # PCLKT2_1
        Pin(39, "", [""]), # PCLKC2_1
        Pin(40, "", [""]),
        Pin(41, "", [""]),
        Pin(42, "", [""]),
        Pin(43, "", [""]),
        Pin(44, "GND", ["GND"]),
        Pin(45, "", [""]),
        Pin(46, "VCCIO2", ["3V3"]),
        Pin(47, "", [""]),
        Pin(48, "SN", [""]),
        Pin(49, "SI/SISPI", [""]),
        Pin(50, "VCC", ["3V3"]),
        Pin(51, "", [""]),
        Pin(52, "", [""]),
        Pin(53, "", [""]),
        Pin(54, "", [""]),
        Pin(55, "VCCIO1", ["3V3"]),
        Pin(56, "GND", ["GND"]),
        Pin(57, "", [""]),
        Pin(58, "", [""]),
        Pin(59, "", [""]),
        Pin(60, "", [""]),
        Pin(61, "NC"),
        Pin(62, "", [""]), # PCLKC1_0
        Pin(63, "", [""]), # PCLKT1_0
        Pin(64, "", [""]),
        Pin(65, "", [""]),
        Pin(66, "", [""]),
        Pin(67, "", [""]),
        Pin(68, "", [""]),
        Pin(69, "", [""]),
        Pin(70, "", [""]),
        Pin(71, "", [""]),
        Pin(72, "GND", ["GND"]),
        Pin(73, "VCCIO1", ["3V3"]),
        Pin(74, "", [""]),
        Pin(75, "", [""]),
        Pin(76, "DONE", [""]),
        Pin(77, "INITN", [""]),
        Pin(78, "", [""]),
        Pin(79, "GND", ["GND"]),
        Pin(80, "VCCIO0", ["3V3"]),
        Pin(81, "PROGRAMN", [""]),
        Pin(82, "JTAGENB", [""]), # GPIO unless JTAG port set to DISABLE (don't do that!)
        Pin(83, "", [""]),
        Pin(84, "", [""]),
        Pin(85, "", [""]), # SDA/PCLKC0_0
        Pin(86, "", [""]), # SCL/PCLKT0_0
        Pin(87, "", [""]), # PCLKC0_1
        Pin(88, "", [""]), # PCLKT0_1
        Pin(89, "NC"),
        Pin(90, "TMS", [""]),
        Pin(91, "TCK", [""]),
        Pin(92, "GND", ["GND"]),
        Pin(93, "VCCIO0", ["3V3"]),
        Pin(94, "TDI", [""]),
        Pin(95, "TDO", [""]),
        Pin(96, "", [""]),
        Pin(97, "", [""]),
        Pin(98, "", [""]),
        Pin(99, "", [""]),
        Pin(100, "VCC", ["3V3"]),
    ],
)
