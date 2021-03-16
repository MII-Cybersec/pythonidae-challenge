## Challenge 03

Spawn an executable, get the stdin and stdout of the process using pipe. Send a string to stdin and get the result from stdout interactively.

## Test

Run [echoer.exe](resources/echoer.exe) (windows) or [echoer](resources/echoer) (linux) and give `MII Cybersec` as argument.

This program will have a infinite loop and will relay any message from stdin to stdout. To terminate, give a string `exit` as input.

Both are 32 bit executable. The source code is available as [echoer.c](resources/echoer.c).

