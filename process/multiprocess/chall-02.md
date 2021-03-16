## Challenge 02

Given a list with `N` elements.

Create a Pool of five processes. Split the list's elements and feed to processes. On each process, print the sublist with ID of the process.

## Remarks

Process Pool is a pool (collection of same type object) of processes that can be access uniformly. As a worker, each process can be set to manipulate same kind of data but different in order of data. This way the processing can be done faster.

To achieve more result, usually tasks would be divided and assigned to different workers. Such tasks would be:

- brute force
- password crack
- scraping and batch download