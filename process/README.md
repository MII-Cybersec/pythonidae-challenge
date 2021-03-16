# Pythonidae Challenge

Learn Python for Cyber Security by completing challenges.

#### Process

This is `Process Set`. This set is related to multiprocessing, multithreading, and other topics to support them. What you need to speed up the code? More worker!

## Table of Content

You will see

- Process or `Multiprocessing`
- `Subprocess`.
- Thread or `Multithreading`

#### Multiprocess

0. fork process, child display message `The Child of Pythonidae` and parent display `The Maker of life`.
1. spawn 5 processes and print their own PID.
2. create a process pool of 5 processes.

#### Subprocess

0. spawn subprocess with an argument.
1. connect output-pipe to subprocess.
2. get the exit code of subprocess.
3. pipe all I/O, give string as input and get output by pipe.

#### Multithread

0. spawn 5 threads and print a unique string for each thread.
1. create list of N elements, spawn 5 threads which consume 1/5 portion of list.
2. create a global-variable, spawn 5 threads which change the value and sleep for random duration. Every thread implement lock.
3. create a queue, spawn 5 threads, each thread will take element from queue.