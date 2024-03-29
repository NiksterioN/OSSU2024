// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// Sets all Register Initial State to 0 

@R2
M=0

// Set i =0
@i
M=0

(LOOP)
// Set D to i
@i
D=M 

// Set D to D = i - R1
@R1 
D=D-M

// If i - R1 > 0; goto END
@END
D;JGE

// Set D to R0
@R0
D=M

// Set R2 = R0 + R2
@R2
M=D+M

// Increment i by 1
@i
M=M+1

@LOOP
0;JMP

(END)
@END
0;JMP