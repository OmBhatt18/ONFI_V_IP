import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer
from commands import txn, cmds

async def generate_clock(dut):
    """Generate clock pulses."""
    cocotb.start_soon(Clock(dut.clk, 1, units="ns").start())

# List of signals with alternate names
signal_names_with_alternates = {
    "RE_x_n": ["RE_x_n", "RE_x_t"],
    "RE_x_c": ["RE_x_c"],
    "W_R_x_n": ["W_R_x_n"],
    "CE_x_n": ["CE_x_n"],
    "Vcc": ["Vcc"],
    "VccQ": ["VccQ"],
    "Vss": ["Vss"],
    "VssQ": ["VssQ"],
    "VREFQ_x": ["VREFQ_x"],
    "Vpp": ["Vpp"],
    "CLE_x": ["CLE_x"],
    "ALE_x": ["ALE_x"],
    "WE_x_n": ["WE_x_n"],
    "CLK_x": ["CLK_x"],
    "WP_x_n": ["WP_x_n"],
    "IO0_0": ["IO0_0", "DQ0_0"],
    "IO8_15": ["IO8_15"],
    "DQS_x_t": ["DQS", "DQS_x_t"],
    "DQS_x_c": ["DQS_x_c"],
    "DBI_x": ["DBI_x"],
    "ENo": ["ENo"],
    "ENi": ["ENi"],
    "VSP_x": ["VSP_x"],
    "R": ["R"],
    "RFT": ["RFT"],
    "NU": ["NU"],
    "NC": ["NC"],
    "ZQ_x": ["ZQ_x"]
}


def fetch_signals(dut):
    found_signals = {}
    unrecognizable_signals = []
    for primary_signal, alternates in signal_names_with_alternates.items():
        for signal_name in alternates:
            if hasattr(dut, signal_name):
                found_signals[primary_signal] = getattr(dut, signal_name)
                break
        else:
            unrecognizable_signals.append(primary_signal)
    return found_signals, unrecognizable_signals

@cocotb.test()
async def test_command_signals(dut):
    await generate_clock(dut)
    await RisingEdge(dut.clk)

    
    signals, unrecognizable_signals = fetch_signals(dut)

    
    cocotb.log.info(f"Total signals found: {len(signals)} out of {len(signal_names_with_alternates)}")
    for name, handle in signals.items():
        cocotb.log.info(f"Signal name: {name}, Handle: {handle}")

   
    if unrecognizable_signals:
        cocotb.log.warning(f"Unrecognizable signals: {', '.join(unrecognizable_signals)}")

    
    await test_read_command(dut, signals)

async def test_read_command(dut, signals):
    
    pass

@cocotb.test()
async def test_reset(dut):
    """Test reset command."""
    await generate_clock(dut)
    await txn('reset')
    await Timer(10, units='ns')

@cocotb.test()
async def test_read_device_id(dut):
    """Test read device ID command."""
    await generate_clock(dut)
    addr = [0x00]  # Example address
    rv = await txn('read_device_id', addr=addr)
    dut._log.info(f"Read Device ID: {rv}")

@cocotb.test()
async def test_block_erase(dut):
    """Test block erase command."""
    await generate_clock(dut)
    addr = [0x00, 0x00, 0x01]  # Example address
    await txn('block_erase', addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_standard_read(dut):
    """Test standard read command."""
    await generate_clock(dut)
    addr = [0x00, 0x00, 0x00, 0x00, 0x00]  # Example address
    rv = await txn('standard_read', addr=addr)
    dut._log.info(f"Standard Read: {rv}")
