## Challenge 01

Given a file `F`.

Open `F` in binary mode. Read the content every 16 bytes and save it to list. If the chunk's size is less than 16, then pad with zero.

## Test

Use [sample-01.bin](resources/sample-01.bin).

The result should be a list with 20 chunks of 16-bytes data.

## Remarks

Some data might be stored in fixed-size chunks. Cryptography is common example, but actually lots of information are stored in structured way. Of course to parse it, we need to know the format or protocol.

To read and parse a consecutive chunks, we can either read block by block, or read whole and slice into chunks in memory.