## Challenge 02

Given a file `F`, integer `O` & `N`.

Open `F` in binary mode. Read the content every block of 16 bytes, start from offset of `O`-th block until at most `N` blocks. Save the result to list. If the chunk's size is less than 16, then pad with zero.

## Test

Use [sample-01.bin](resources/sample-01.bin).

The result should be a list with 20 chunks of 16-bytes data.

## Remarks

Reading data is not always started from the beginning of the file. Offset and count is used to limit what and where to get data.

This operation is used frequently when dealing with structured data, especially indexed data.