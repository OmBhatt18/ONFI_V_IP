module nand_controller (
    input clk,
    input  wire RB_x_n,
    output wire RE_x_n,
    output wire RE_x_c,
    output wire WR_x_n,
    output wire CE_x_n,
    output wire Vcc,
    output wire VccQ,
    output wire Vss,
    output wire VssQ,
    output wire VREFQ_x,
    output wire Vpp,
    output wire CLE_x,
    output wire ALE_x,
    output wire WE_x_n,
    output wire CLK_x,
    output wire WP_x_n,

    inout wire IO0_0,
    inout wire IO1_0,
    inout wire IO2_0,
    inout wire IO3_0,
    inout wire IO4_0,
    inout wire IO5_0,
    inout wire IO6_0,
    inout wire IO7_0,

    inout wire IO8,
    inout wire IO9,
    inout wire IO10,
    inout wire IO11,
    inout wire IO12,
    inout wire IO13,
    inout wire IO14,
    inout wire IO15,

    inout wire IO0_1,
    inout wire IO1_1,
    inout wire IO2_1,
    inout wire IO3_1,
    inout wire IO4_1,
    inout wire IO5_1,
    inout wire IO6_1,
    inout wire IO7_1,

    inout wire DQS,
    inout wire DQS_x_c,
    inout wire DBI_x,

    input wire ENo,
    output wire ENi,
    inout wire VSP_x,
    input wire R,
    input wire RFT,
    inout wire NU,
    inout wire NC,
    inout wire ZQ_x
);

initial begin
    $display("NAND Controller");
    $dumpfile("waveform.vcd");
    $dumpvars(0, nand_controller);
end

endmodule

