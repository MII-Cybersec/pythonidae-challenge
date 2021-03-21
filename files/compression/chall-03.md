## Challenge 03

Given a compressed file `F`.

Read the content of decompressed `F` using `BZIP2`.

## Test

Use [sample-03.bin](resources/sample-03.bin).

It should be decompressed to `b"Pythonidae with BZIP2"`.

## Remarks

`BZIP2` is compression format used by `.bz2` file format.

BZIP2 is not archive format. It can only compress single data (file). To compress multiple file, the files are usually archived using `TAR` or other format then compressed by BZIP2.

References:

- [wikipedia](https://en.wikipedia.org/wiki/Bzip2)