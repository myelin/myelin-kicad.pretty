# Xilinx XC95144XL CPLD, in 144-pin 0.5mm TQFP package
cpld = myelin_kicad_pcb.Component(
    footprint="myelin-kicad:xilinx_tqg144",
    identifier="CPLD1",
    value="XC95144XL-144TQG",
    buses=[""],
    pins=[
        Pin(  1, "VCCIO_2V5_3V3", "3V3")
        Pin(  2, "P2.5-I/O/GTS3", "I/O/GTS3")
        Pin(  3, "P2.6-I/O/GTS4", "I/O/GTS4")
        Pin(  4, "P2.4", [""])
        Pin(  5, "P2.8-I/O/GTS1", "I/O/GTS1")
        Pin(  6, "P2.9-I/O/GTS2", "I/O/GTS2")
        Pin(  7, "P2.10", [""])
        Pin(  8, "VCCINT_3V3", "3V3")
        Pin(  9, "P2.11", [""])
        Pin( 10, "P2.12", [""])
        Pin( 11, "P2.14", [""])
        Pin( 12, "P2.13", [""])
        Pin( 13, "P2.15", [""])
        Pin( 14, "P2.16", [""])
        Pin( 15, "P2.17", [""])
        Pin( 16, "P1.2", [""])
        Pin( 17, "P1.3", [""])
        Pin( 18, "GND", "GND")
        Pin( 19, "P1.5", [""])
        Pin( 20, "P1.6", [""])
        Pin( 21, "P1.8", [""])
        Pin( 22, "P1.9", [""])
        Pin( 23, "P1.1", [""])
        Pin( 24, "P1.11", [""])
        Pin( 25, "P1.4", [""])
        Pin( 26, "P1.12", [""])
        Pin( 27, "P1.14", [""])
        Pin( 28, "P1.15", [""])
        Pin( 29, "GND", "GND")
        Pin( 30, "P1.17-I/O/GCK1", "I/O/GCK1")
        Pin( 31, "P1.10", [""])
        Pin( 32, "P3.2-I/O/GCK2", "I/O/GCK2")
        Pin( 33, "P3.5", [""])
        Pin( 34, "P3.6", [""])
        Pin( 35, "P1.16", [""])
        Pin( 36, "GND", "GND")
        Pin( 37, "VCCIO_2V5_3V3", "3V3")
        Pin( 38, "P3.8-I/O/GCK3", "I/O/GCK3")
        Pin( 39, "P3.1", [""])
        Pin( 40, "P3.9", [""])
        Pin( 41, "P3.3", [""])
        Pin( 42, "VCCINT_3V3", "3V3")
        Pin( 43, "P3.11", [""])
        Pin( 44, "P3.4", [""])
        Pin( 45, "P3.12", [""])
        Pin( 46, "P3.7", [""])
        Pin( 47, "GND", "GND")
        Pin( 48, "P3.10", [""])
        Pin( 49, "P3.14", [""])
        Pin( 50, "P3.15", [""])
        Pin( 51, "P3.17", [""])
        Pin( 52, "P5.2", [""])
        Pin( 53, "P5.5", [""])
        Pin( 54, "P5.6", [""])
        Pin( 55, "VCCIO_2V5_3V3", "3V3")
        Pin( 56, "P5.8", [""])
        Pin( 57, "P5.9", [""])
        Pin( 58, "P5.11", [""])
        Pin( 59, "P5.3", [""])
        Pin( 60, "P5.12", [""])
        Pin( 61, "P5.14", [""])
        Pin( 62, "GND", "GND")
        Pin( 63, "TDI", "cpld_TDI")
        Pin( 64, "P5.15", [""])
        Pin( 65, "TMS", "cpld_TMS")
        Pin( 66, "P5.7", [""])
        Pin( 67, "TCK", "cpld_TCK")
        Pin( 68, "P5.10", [""])
        Pin( 69, "P5.17", [""])
        Pin( 70, "P5.13", [""])
        Pin( 71, "P7.2", [""])
        Pin( 72, "GND", "GND")
        Pin( 73, "VCCIO_2V5_3V3", "3V3")
        Pin( 74, "P7.5", [""])
        Pin( 75, "P7.3", [""])
        Pin( 76, "P7.6", [""])
        Pin( 77, "P7.7", [""])
        Pin( 78, "P7.8", [""])
        Pin( 79, "P7.10", [""])
        Pin( 80, "P7.9", [""])
        Pin( 81, "P7.13", [""])
        Pin( 82, "P7.11", [""])
        Pin( 83, "P7.16", [""])
        Pin( 84, "VCCINT_3V3", "3V3")
        Pin( 85, "P7.12", [""])
        Pin( 86, "P7.14", [""])
        Pin( 87, "P7.15", [""])
        Pin( 88, "P7.17", [""])
        Pin( 89, "GND", "GND")
        Pin( 90, "GND", "GND")
        Pin( 91, "P8.2", [""])
        Pin( 92, "P8.5", [""])
        Pin( 93, "P8.6", [""])
        Pin( 94, "P8.8", [""])
        Pin( 95, "P8.3", [""])
        Pin( 96, "P8.9", [""])
        Pin( 97, "P8.4", [""])
        Pin( 98, "P8.11", [""])
        Pin( 99, "GND", "GND")
        Pin(100, "P8.12", [""])
        Pin(101, "P8.10", [""])
        Pin(102, "P8.14", [""])
        Pin(103, "P8.13", [""])
        Pin(104, "P8.15", [""])
        Pin(105, "P8.17", [""])
        Pin(106, "P6.2", [""])
        Pin(107, "P8.16", [""])
        Pin(108, "GND", "GND")
        Pin(109, "VCCIO_2V5_3V3", "3V3")
        Pin(110, "P6.5", [""])
        Pin(111, "P6.4", [""])
        Pin(112, "P6.6", [""])
        Pin(113, "P6.8", [""])
        Pin(114, "GND", "GND")
        Pin(115, "P6.10", [""])
        Pin(116, "P6.9", [""])
        Pin(117, "P6.16", [""])
        Pin(118, "P4.1", [""])
        Pin(119, "P6.11", [""])
        Pin(120, "P6.12", [""])
        Pin(121, "P6.14", [""])
        Pin(122, "TDO", "cpld_TDO")
        Pin(123, "GND", "GND")
        Pin(124, "P6.15", [""])
        Pin(125, "P6.17", [""])
        Pin(126, "P4.2", [""])
        Pin(127, "VCCIO_2V5_3V3", "3V3")
        Pin(128, "P4.5", [""])
        Pin(129, "P4.6", [""])
        Pin(130, "P4.8", [""])
        Pin(131, "P4.9", [""])
        Pin(132, "P4.11", [""])
        Pin(133, "P4.3", [""])
        Pin(134, "P4.12", [""])
        Pin(135, "P4.10", [""])
        Pin(136, "P4.14", [""])
        Pin(137, "P4.13", [""])
        Pin(138, "P4.15", [""])
        Pin(139, "P4.16", [""])
        Pin(140, "P4.17", [""])
        Pin(141, "VCCINT_3V3", "3V3")
        Pin(142, "P2.1", [""])
        Pin(143, "P2.2-I/O/GSR", "I/O/GSR")
        Pin(144, "GND", "GND")
    ],
)
cpld_caps = [
    myelin_kicad_pcb.C0805("100n", "3V3", "GND", ref="CC%d" % n)
    for n in range(10)
]
myelin_kicad_pcb.update_xilinx_constraints(cpld, os.path.join(here, PATH_TO_CPLD, "constraints.ucf"))