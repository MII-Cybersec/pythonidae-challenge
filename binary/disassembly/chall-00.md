## Challenge 00

Given sequence of byte representing shellcode.

Disassemble the shellcode, use `0x1000` as base address. At least, these information should be present:

- address
- raw bytes
- instruction

Note: 

- feel free to use any external libraries you want.
- read the file in binary mode. 

## Test 

Use the shellcode [sample-00.bin](resources/sample-00.bin).

This is `linux/x86` code. See also the [source code](resources/sample-00.nasm)

## Remarks

Disassembling code is one of important aspects in reverse engineering, program analysis, and exploit development. The goal is to revert the sequence of bytes back to the assembly mnemonic, in hope to understand the code better.

Disassemble can be done on whole program or portion of code. The code is mapped to memory address range, so (relative) jump can be resolved. 

Some libraries that can be used for disassembly:

- amoco (arm, avr, x86)
- capstone (arm, aarch64, mips, ppc, riscv, sparc, x86, ...)
- distorm3 (x86/x64)
- miasm (arm, mips, msp430, sh4, x86)

