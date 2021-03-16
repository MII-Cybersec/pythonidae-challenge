## Challenge 01

Given sequence of byte representing shellcode.

Count all mnemonic and create the statistic of occurrence.

Note: 

- feel free to use any external libraries you want.
- read the file in binary mode.

## Test 

Use shellcode [sample-01.bin](resources/sample-01.bin).

This is `linux/x86` code. See also the [source code](resources/sample-01.nasm)

## Remarks

Identifying instructions is essentially important for program analysis. For a script to analyze program, it's not enough to just disassemble. The analysis script should be aware to the instructions processed.