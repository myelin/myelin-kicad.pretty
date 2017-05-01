OUTPUTS=acorn_electron_cartridge_socket.kicad_mod \
	issi_32l_450mil_sop.kicad_mod \
	pro_micro.kicad_mod \
	sst_plcc32_nh.kicad_mod \
	via_single.kicad_mod \
	xilinx_vqg44.kicad_mod \
	xilinx_vqg64.kicad_mod

all: $(OUTPUTS)

via_single.kicad_mod: via_arrays.py myelin_kicad_mod.py
	python $<

%.kicad_mod: %.py myelin_kicad_mod.py
	python $<
