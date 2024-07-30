SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/dummy_dut.v
TOPLEVEL?= dummy_dut
MODULE = test_onfi
onfi:
	$(MAKE) sim MODULE=test_onfi
include $(shell cocotb-config --makefiles)/Makefile.sim

