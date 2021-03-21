## Challenge 00

Given a compressed data `D`.

Read the content of decompress `D` with `DEFLATE` algorithm.

## Test

Use [sample-00.bin](resources/sample-00.bin).

It should be decompressed to `b"Pythonidae DEFLATE compression"`.

## Remarks

DEFLATE is lossless data compression format which compress of a series of blocks. Each block is compressed using combination of `LZ77` algorithm and `Huffman coding`.

DEFLATE is used in used and implemented in several format, such as:

- ZIP archive files.
- gzip compressed files.
- PNG image files.

Reference:
- [IETF](https://tools.ietf.org/html/rfc1951)
- [wikipedia](https://en.wikipedia.org/wiki/Deflate)