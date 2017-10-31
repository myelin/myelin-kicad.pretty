OUTPUTS=acorn_electron_cartridge_socket.kicad_mod \
	bbc_1mhz_bus_board.kicad_mod \
	issi_32l_450mil_sop.kicad_mod \
	fci_sd_card_socket.kicad_mod \
	hirose_micro_sd_card_socket.kicad_mod \
	micro_usb_b_smd_molex.kicad_mod \
	pro_micro.kicad_mod \
	sst_plcc32_nh.kicad_mod \
	usb_a_host_pth_amphenol.kicad_mod \
	via_single.kicad_mod \
	xilinx_vqg44.kicad_mod \
	xilinx_vqg64.kicad_mod

default: all

all: $(OUTPUTS)

via_single.kicad_mod: via_arrays.py myelin_kicad_mod.py
	python $<

%.kicad_mod: %.py myelin_kicad_mod.py
	python $<
