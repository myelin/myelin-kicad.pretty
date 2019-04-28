OUTPUTS=acorn_electron_cartridge_socket.kicad_mod \
	bbc_1mhz_bus_board.kicad_mod \
	bbc_master_econet_module.kicad_mod \
	bourns_cat16_j8_resistor_array.kicad_mod \
	cherry_mx_pcb_mount.kicad_mod \
	cypress_lae064_fbga.kicad_mod \
	dgh255q5r5.kicad_mod \
	din_5_econet_pcb_mount.kicad_mod \
	minidin_6_ps2_pcb_mount.kicad_mod \
	header_2x20_100mil.kicad_mod \
	issi_32l_450mil_sop.kicad_mod \
	fci_sd_card_socket.kicad_mod \
	hirose_micro_sd_card_socket.kicad_mod \
	jtag_shrouded_2x5.kicad_mod \
	lattice_tn100.kicad_mod \
	lattice_ftg256_fbga.kicad_mod \
	intel_ubga169.kicad_mod \
	lcsoft_mini_flipped.kicad_mod \
	micro_usb_b_smd_molex.kicad_mod \
	pomona_5401_plcc68_clip.kicad_mod \
	pro_micro.kicad_mod \
	raspberry_pi_zero_flipped.kicad_mod \
	sdram_54tfbga.kicad_mod \
	so8_pcf8583t_7.5x7.5mm.kicad_mod \
	sst_plcc32_nh.kicad_mod \
	ti_zrd_54_pbga.kicad_mod \
	usb_a_host_pth_amphenol.kicad_mod \
	via_single.kicad_mod \
	xilinx_csg144.kicad_mod \
	xilinx_vqg44.kicad_mod \
	xilinx_vqg64.kicad_mod

default: all

all: $(OUTPUTS)

via_single.kicad_mod: via_arrays.py myelin_kicad_mod.py
	python $<

%.kicad_mod: %.py myelin_kicad_mod.py
	python $<
