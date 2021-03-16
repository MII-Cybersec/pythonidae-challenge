## Challenge 01

Spawn an executable. Capture the stdout, redirect the output into other stream or pipe.

Note:
- you can open a file as destination stream.
- no operator `>` or similar involved in the execution of script.

## Test

Run [runme.exe](resources/runme.exe) (windows) or [runme](resources/runme) (linux) and give `MII Cybersec` as argument.

All output should be stored into file.

Both are 32 bit executable. The source code is available as [runme.c](resources/runme.c).