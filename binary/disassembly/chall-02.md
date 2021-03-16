## Challenge 02

Given sequence of byte representing shellcode.

Identify which syscall number is called.

Note: 

- feel free to use any external libraries you want.
- read the file in binary mode.

## Test 

Use shellcode [sample-02.bin](resources/sample-02.bin).

This is `linux/x86` code. See also the [source code](resources/sample-02.nasm).

There are 5 (five) syscall invocation, which has 5 different syscall number.

## Remarks

Syscalls, or System Calls, are requests of kernel's services, identified by numbers. Different operating system might provide different services. But some popular and common services: process control, file management, and communication.

Identifying syscalls are useful when analyzing shellcode, especially in predicting what it will do.

Different operating system provide different syscalls. Even for different architecture, the number might be different. In this case consult documentation for the correct platform.