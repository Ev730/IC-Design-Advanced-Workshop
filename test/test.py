# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    await RisingEdge(dut.clk)
    assert int(dut.uo_out.value) == 0, f"Expected 0, got {int(dut.uo_out.value)}"

    # Check a few values
    for expected in range(1, 6);
        await RisingEdge(dut.clk)
        got = int(dut.uo_out.value)
        assert got == expected, f"Expected {expected}, got {got}"
        dut._log.info(f"Counter Value = {got}")
