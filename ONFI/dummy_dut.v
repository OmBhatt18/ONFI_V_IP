module dummy_dut(input clk,
input wire RE_x_t,
    input wire RE_x_c,
    input wire W_R_x_n,
    input wire CE_x_n,
    input wire Vcc,
    input wire VccQ,
    input wire Vss,
    input wire VssQ,
    input wire VREFQ_x,
    input wire Vpp,
    input wire CLE_x,
    input wire ALE_x,
    input wire WE_x_n,
    input wire CLK_x,
    input wire WP_x_n,
    inout wire [7:0] IO0_0,
    inout wire [7:0] IO8_15,
    inout wire DQS_x_t,
    inout wire DQS_x_c,
    inout wire DBI_x,
    output wire ENo,
    input wire ENi,
    inout wire VSP_x,
    inout wire R,
    inout wire RFT,
    inout wire NU,
    inout wire NC,
    inout wire ZQ_x

);
    initial begin
        $display("Dummy DUT");
        $dumpfile("waveform.vcd"); 
        $dumpvars(0, dummy_dut); 
    end
endmodule
