## Challenge 00

Spawn a child process. The child process should print `The Child of Pythonidae` and the parent process should print `The Maker of Life`.

Note: In Windows, `os.fork()` is not usable. Try a generic solution.

## Remarks

Process is an instance of a program that is being executed. By default processes are not sharing any memory or data and use Inter-Process Communication to communicate with each other.

To achieve concurrency, a program can use multiple process of similar program and work together to process the workload. The task is divided into several worker processes and usually controlled by a master.