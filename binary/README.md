# Pythonidae Challenge

Learn Python for Cyber Security by completing challenges.

## Binary

This is `Binary Set`. If you are confident in learning hex, then this challenge is right for you.

This challenge consists of several activites relate to binary analysis, exploit development, and shellcodes creation utilities.

## Table of Content

You will see

- Executable `parsing`
- `Disassembly`
- `Interoperable`

#### Executable Parsing

0. open executable (PE/ELF) and determine the target architecture.
1. get the entrypoint address from executable (PE/ELF).
2. list all sections with their size and permission.
3. list the name and address of all imported functions.
4. compute the entropy of each section.
5. list all printable string which length exceed certain number.
6. list all entries (name, offset) of relocation table.

#### Disassembly

0. read shellcode file as blob and disassemble.
1. count the frequency of each instruction.
2. identify invoked syscall by syscall number.
3. create statistic of registers (source, destination).
4. list all memory addresses.
5. map all branching operations as (source, destination) tuple.

#### Interoperable

0. call function from shared library (DLL / SO) based on function name.
1. get the return value of function call.
2. pass mutable string and print string after function call.
3. pass structure to function.