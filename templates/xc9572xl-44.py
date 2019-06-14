# Xilinx XC9572XL CPLD, in 44-pin VQFP package
# https://www.xilinx.com/support/documentation/data_sheets/ds057.pdf
# VQ44 package: https://www.xilinx.com/support/documentation/package_specs/vq44.pdf
cpld = Component(
    footprint="myelin-kicad:xilinx_vqg44",
    identifier="U?",
    value="XC9572XL-10VQG44C",
    desc="IC CPLD Xilinx 72MC 44-pin; https://www.digikey.com/products/en?keywords=122-1448-ND",
    pins=[
        Pin(39, "P1.2", [""]),
        Pin(40, "P1.5", [""]),
        Pin(41, "P1.6", [""]),
        Pin(42, "P1.8", [""]),
        Pin(43, "P1.9-GCK1", [""]),
        Pin(44, "P1.11-GCK2", [""]),
        Pin(1, "P1.14-GCK3", [""]),
        Pin(2, "P1.15", [""]),
        Pin(3, "P1.17", [""]),
        Pin(4, "GND", ["GND"]),
        Pin(5, "P3.2", [""]),
        Pin(6, "P3.5", [""]),
        Pin(7, "P3.8", [""]),
        Pin(8, "P3.9", [""]),
        Pin(9, "TDI", ["cpld_TDI"]),
        Pin(10, "TMS", ["cpld_TMS"]),
        Pin(11, "TCK", ["cpld_TCK"]),
        Pin(12, "P3.11", [""]),
        Pin(13, "P3.14", [""]),
        Pin(14, "P3.15", [""]),
        Pin(15, "VCCINT_3V3", ["3V3"]),
        Pin(16, "P3.17", [""]),
        Pin(17, "GND", ["GND"]),
        Pin(18, "P3.16", [""]),
        Pin(19, "P4.2", [""]),
        Pin(20, "P4.5", [""]),
        Pin(21, "P4.8", [""]),
        Pin(22, "P4.11", [""]),
        Pin(23, "P4.14", [""]),
        Pin(24, "TDO", ["cpld_TDO"]),
        Pin(25, "GND", ["GND"]),
        Pin(26, "VCCIO_2V5_3V3", ["3V3"]),
        Pin(27, "P4.15", [""]),
        Pin(28, "P4.17", [""]),
        Pin(29, "P2.2", [""]),
        Pin(30, "P2.5", [""]),
        Pin(31, "P2.6", [""]),
        Pin(32, "P2.8", [""]),
        Pin(33, "P2.9-GSR", [""]),
        Pin(34, "P2.11-GTS2", [""]),
        Pin(35, "VCCINT_3V3", ["3V3"]),
        Pin(36, "P2.14-GTS1", [""]),
        Pin(37, "P2.15", [""]),
        Pin(38, "P2.17", [""]),
    ],
)
cpld_cap1 = C0805("100n", "3V3", "GND", ref="C?")
cpld_cap2 = C0805("100n", "3V3", "GND", ref="C?")
myelin_kicad_pcb.update_xilinx_constraints(cpld, os.path.join(here, PATH_TO_CPLD, "constraints.ucf"))

cpld_jtag = Component(
    footprint="Pin_Headers:Pin_Header_Straight_2x05_Pitch2.54mm",
    identifier="CON?",
    value="jtag",
    pins=[
        Pin(1, "TCK", ["cpld_TCK"]), # top left
        Pin(2, "GND", ["GND"]), # top right
        Pin(3, "TDO", ["cpld_TDO"]),
        Pin(4, "3V3", ["3V3"]),
        Pin(5, "TMS", ["cpld_TMS"]),
        Pin(6, "NC"),
        Pin(7, "NC"),
        Pin(8, "NC"),
        Pin(9, "TDI", ["cpld_TDI"]),
        Pin(10, "GND", ["GND"]),
    ],
)

regulator = Component(
    footprint="TO_SOT_Packages_SMD:SOT-89-3",
    identifier="U?",
    value="MCP1700T-3302E/MB",
    pins=[
        Pin(2, "VIN", ["5V"]),
        Pin(3, "VOUT", ["3V3"]),
        Pin(1, "GND", ["GND"]),
    ],
)
reg_in_cap = C0805("1u", "5V", "GND", ref="C?")
reg_out_cap = C0805("1u", "3V3", "GND", ref="C?")
