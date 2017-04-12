OUTPUTS=acorn_electron_cartridge_socket.kicad_mod xilinx_vqg44.kicad_mod pro_micro.kicad_mod sst_plcc32_nh.kicad_mod

all: $(OUTPUTS)

%.kicad_mod: %.py myelin_kicad_mod.py
	python $<