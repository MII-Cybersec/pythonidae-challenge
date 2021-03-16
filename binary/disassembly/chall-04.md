## Challenge 04

Given sequence of byte representing shellcode.

List all memory address involved in every instructions and specify the operation (read/write) to the address.

Sample expected result:

```
Write to 0x11223344
Read from 0x11223344
```

Only take the instruction which has memory access (direct or indirect by register). In case of indirect memory access (using register), try to get the value of register to determine the memory address.

Note: 

- feel free to use any external libraries you want.
- read the file in binary mode.

## Test 

Use executable [sample-03](resources/sample-03).

This is `linux/x86` binary. See also the [source code](resources/sample-03.nasm).

This executable is modified version of `execve` shellcode. Instead of setting buffer on stack, we use the `.bss` section.

## Remarks

Identifying memory address is useful to track the value in `Data-Flow`, `Taint Analysis`, and other analyses. The goal might be varying, but the common purpose is to know the value of memory at a time.

By identifying memory address and furthermore the value read/write, a deeper analysis on behavior can be done.