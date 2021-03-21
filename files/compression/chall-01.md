## Challenge 01

Given acompressed data `D`.

Read the content of decompress `D` with `LZMA` algorithm.

## Test

Use [sample-01.bin](resources/sample-01.bin).

It should be decompressed to `b"Pythonidae LZMA compression"`.

## Remarks

LZMA (Lempel-Ziv-Markov chain Algorithm) is lossless data compression algorithm. The compressed stream is a stream of bits, encoded using an adaptive binary range coder, divided into blocks (packets).

LZMA is used and implemented in several format, such as:

- `7z` archive files.
- `xz` archive files.

Reference:
- [wikipedia](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm)