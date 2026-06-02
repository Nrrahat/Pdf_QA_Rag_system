# Computer Peripherals, Interfacing, and IoT 

**==> picture [707 x 468] intentionally omitted <==**

**==> picture [714 x 474] intentionally omitted <==**

**==> picture [701 x 468] intentionally omitted <==**

**==> picture [712 x 480] intentionally omitted <==**

**==> picture [700 x 450] intentionally omitted <==**

**==> picture [697 x 486] intentionally omitted <==**

**==> picture [706 x 474] intentionally omitted <==**

**==> picture [692 x 486] intentionally omitted <==**

**==> picture [695 x 492] intentionally omitted <==**

## _**Outline**_ 

- 8085 Era and Features 

- 8085 

   - Block diagram (Data Path) 

   - Bus Structure 

   - Register Structure 

- Instruction Set of 8085 

- Sample program of 8085 

- Simulator & Kit for 8085 

## _**8085 Microprocessor**_ 

- 8 Bit CPU 

- 3-6Mhz 

- Simpler design: Single Cycle CPU 

- ISA = Pre x86 design (Semi CISC) 

- 40 Pin Dual line Package 

- 16 bit address 

- 6 registers: B, C, D, E, H,L 

- Accumulator 8 bit 

## _**8085 Microprocessor Architecture**_ 

**==> picture [699 x 477] intentionally omitted <==**

**----- Start of picture text -----**<br>
ReSeT6.5<br>INTR INTA  RST5.5   RST7.5  [ TRAP ]  SID   SOD<br>Interrupt Control   Serial I/O Control<br>                                                  Bus 8 Bit<br>MUX<br>ACC  tmp R<br>IR  W  Z<br>B  C<br>Flag<br>I Decode  D  E<br>&   H  L<br>M/C<br>ALU  Encodin SP<br>PC<br>g<br>Inc/Dec. ter<br> Add latch<br>Timing and Control<br>Add Buff  Data/Add Buff<br>**----- End of picture text -----**<br>


## _**The 8085 Bus Structure**_ 

**==> picture [650 x 351] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>15<br>         Address Bus (16bit)<br>A<br>0<br>Memory  I/P<br>8085<br>MPU<br>O/P<br>D7<br>Data Bus (8bit)<br>D0<br>Control Bus (8bit)<br>**----- End of picture text -----**<br>


## _**8085 Bus Structure**_ 

- Address Bus : Consists of 16 address lines: A – A 0 15 

   - Address locations: 0000 (hex) – FFFF (hex) 

   - Can access 64K ( = 2[16] ) bytes of memory,  each byte has 8 bits 

   - Can access  64K  8 bits of memory 

   - Use memory to map I/O,  Same instructions to use for accessing I/O devices and memory 

- Data Bus : Consists of 8 data lines: D – D 0 7 

   - Operates in bidirectional mode 

   - The data bits are sent from the MPU to I/O & vice versa 

   - Data range: 00 (hex) – FF (hex) 

- Control Bus: 

   - Consists of various lines carrying the control signals such as read / write enable, flag bits 

## _**8085 Registers**_ 

## • Registers: 

- Six general purpose 8-bit registers: B, C, D, E, H,L 

- Combined as register pairs to perform 16-bit operations: BC, DE, HL 

- Registers are programmable (load, move, etc.) 

**==> picture [137 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
B  C<br>D  E<br>H  L<br>SP<br>PC<br>**----- End of picture text -----**<br>


- Stack Pointer (SP) 

- Accumulator & Flag Register 

   - (Zero, Sign, Carry, Parity, AuxCarry) 

- Program Counter (PC) 

   - Contains the memory address (16 bits) of the instruction that will be executed in the next step. 

## _**How instruction executed**_ 

- All instructions (of a program) are stored in memory. 

- To run a program, the individual instructions must  be read from the memory in sequence, and executed. 

   - Program counter puts the 16-bit memory address of the instruction on the address bus 

   - Control unit sends the Memory Read Enable signal to   access the memory 

   - The 8-bit instruction stored in memory is placed on the data bus and transferred to the instruction decoder 

   - Instruction is decoded and executed 

## _**Instruction Set of 8085**_ 

# • Arithmetic Operations 

   - add, sub, inr/dcr 

- Logical operation 

   - and, or, xor, rotate, compare, complement 

- Branch operation 

   - Jump, call, return 

- Data transfer/Copy/Memory operation/IO 

   - MOV, MVI, LD, ST,  OUT 

## _**Copy/Mem/IO operation**_ 

- MVI    R, 8 bit _// load immediate data_ 

- MOV   R1, R2 _// Example MOV  B, A_ 

- • MOV   R   M _// Copy to R from 0(HL Reg) Mem_ 

- • MOV   M   R _// Copy from R to  0(HL Reg) Mem_ 

- LDA     16 bit _// load A from 0(16bit)_ 

- STA      16 bit _// Store A to 0(16bit)_ 

- LDAX    Rp _// load  A from 0(Rp), Rp=RegPair_ 

- STAX     Rp _// Store A to 0(Rp)_ 

- LXI  Rp  16bit _// load immediate to Rp_ 

- IN 8bit _// Accept data to A from port 0(8bit)_ 

- OUT 8 bit _// Send data of A to  port 0(8bit)_ 

## _**Arithmetic Operation**_ 

- ADD R _// Add A = A + B.reg_ 

- ADI   8bit _// Add A= A + 8bit_ 

- ADD M _// Add  A=A + 0(HL)_ 

- SUB  R _// Sub A = A -B.reg_ 

- • SUI   8bit _// Sub A= A - 8bit_ 

- • SUB M _// Sub  A=A - 0(HL)_ 

- INR    R _//  R = R+1_ 

- • INR  M _//  0(HL)=0(HL)+1_ 

- • DCR    R _// R = R-1_ 

- • DCR  M _// 0(HL)=0(HL)-1_ 

- • INX     Rp _//  Rp=Rp+1_ 

- • DCX     Rp _//  Rp=Rp-1_ 

## _**Other Operations**_ 

- Logic operations 

   - ANA R          ANI 8bit   ANA M 

   - ORA, ORI, XRA, XRI 

   - CMP R // compare with R with ACC 

   - CPI 8bit // compare 8 bit with ACC 

- Branch operations 

   - JMP 16bit, CALL 16 bit 

   - JZ 16bit,  JNZ 16bit, JC 16bit, JNC 16 bit 

   - RET 

- Machine Control operations 

   - HLT, NOP, POP, PUSH 

## _**Assumption**_ 

- RAM Memory is interfaced 

- Instructions are stored in memory 

- One I/O display port is interfaced to display data of ACC 

## _**Simple Assembly Program**_ 

MVI   A, 24H _// load Reg  ACC with 24H_ MVI   B , 56H _// load Reg B with 56H_ ADD   B _// ACC= ACC+B_ OUT 01H _// Display ACC contents on port 01H_ HALT _// End the program_ 

Result: 7A (All are in Hex) DAA operation for Decimal Adjust    A+6=10H 

## _**Flowchart to multiply two number**_ 

Start 

**==> picture [28 x 27] intentionally omitted <==**

LDA   2000     // Load multiplicant to accumulator MOV  B,A       // Move multiplicant from A(acc) to B register 

**==> picture [28 x 27] intentionally omitted <==**

LDA   2001    // Load multiplier to accumulator MOV  C,A      // Move multiplier from A to C 

**==> picture [28 x 27] intentionally omitted <==**

MOV  C,A      // Move multiplier from A to C MVI   A,00    // Load immediate value 00 to ACC 

**==> picture [314 x 21] intentionally omitted <==**

ADD    B     // Add B(multiplier) with A DCR    C      // Decrement C, it act as a counter 

**==> picture [28 x 27] intentionally omitted <==**

JNZ     L   // Jump to L if C!=0 

**==> picture [92 x 21] intentionally omitted <==**

**==> picture [28 x 27] intentionally omitted <==**

STA    2010   // Store result in to memory HLT                // End 

_**Code to multiply two number**_ LDA   2000     // Load multiplicant to accumulator MOV  B,A       // Move multiplicant from A(acc) to B register LDA   2001    // Load multiplier to accumulator MOV  C,A      // Move multiplier from A to C MVI   A,00    // Load immediate value 00 to a L:   ADD    B      // Add B(multiplier) with A DCR    C         // Decrement C, it act as a counter JNZ     L          // Jump to L if C reaches 0 STA    2010   // Store result in to memory HLT                // End 

## _**Factorial of a Program**_ 

LXI SP, 27FFH ; Initialize stack pointer LDA 2200H ; Get the number CPI 02H ; Check if number is greater than 1 JC LAST 

MVI D, 00H ; Load number as a result MOV E, A DCR A 

MOV C,A ; Load counter one less than number CALL FACTO ; Call subroutine FACTO **XCHG ; Get the result in HL  // HL with DE SHLD 2201H ; Store result in the memory   // store HL at 0(16bit)** JMP END 

LAST: LXI H, 000lH ; Store result = 01 END: **SHLD 2201H** HLT 

## _**Sub Routine for FACTORIAL**_ 

FACTO: LXI H, 0000H MOV B, C ; Load counter BACK: **DAD D   // double add ; HL=HL+DE** DCR B JNZ BACK ; Multiply by successive addition **XCHG ; Store result in DE // HL with DE** DCR C ; Decrement counter CNZ FACTO ; Call subroutine FACTO RET ; Return to main program 

## _**8085 Simulator & Kit**_ 

- 8085 Simulator is available 

   - Course website 

- 8085 Kit is available in HW Lab (CS422) 

   - First test the program on Simulator and then go for the HW 

   - Sometime Kit have Driver, IDE and Assembler 

**==> picture [703 x 492] intentionally omitted <==**

