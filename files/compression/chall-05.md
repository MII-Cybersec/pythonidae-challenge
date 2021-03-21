## Challenge 05

Given a sequence of bytes representing a `ZIP` file.

List all files in archive and read the content of first file.

## Test

use [sample-05.zip](resources/sample-05.zip).

It should be 2 files `file-01` and `file-02`.

## Remarks

`ZIP` is a archive format to join several files and directories into single file.

`ZIP` support lossless data compression. Despite support various compression algorithms, `DEFLATE` is the most common algorithm.

References:

- [wikipedia](https://en.wikipedia.org/wiki/ZIP_(file_format))