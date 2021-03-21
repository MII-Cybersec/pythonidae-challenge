## Challenge 02

Given a compressed data `D`.

Read the content of decompressed `D` using `GZIP`.

## Test

Use [sample-02.bin](resources/sample-02.bin).

It should be decompressed to `b"Pythonidae in GZIP"`.

## Remarks

`GZIP` is compression format based on `DEFLATE` algorithm. GZIP is used by `.gz` file format.

GZIP is not archive format. It can only compress single data (file). To compress multiple file, the files are usually archived using `TAR` or other format then compressed by GZIP.

References:

- [wikipedia](https://en.wikipedia.org/wiki/Gzip)