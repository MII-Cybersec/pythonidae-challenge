## Challenge 00

Given a file `F`.

Read the content of `F` line by line and represent it as list.

Note: Make sure the line are properly trimmed.

## Test

Use [sample-00.txt](resources/sample-00.txt).

It should create a list of 20 strings.

## Remarks

A good script implement algorithm which works on any valid data. Such example can be found on brute-force script where the logic is simple and work with any wordlist. Each line of wordlist is a username, password, or any words used as payload. 

There are several strategies for reading text files. We can read line by line, or we can read all the content then split in memory.