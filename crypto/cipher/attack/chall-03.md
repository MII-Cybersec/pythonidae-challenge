## Challenge 03

Given a string `S`. 

Detect whether the string has been encrypted by `AES/ECB`.

Note:
- only predict whether the data is encrypted by `AES/ECB` or not.
- use statistic analysis on the blocks.

## Remarks

`ECB (Electronic Code Book)` is an encryption mode which divide message into blocks and each block is encrypted separately. The result of one block won't affecting other block.

ECB is stateless and deterministic, which 16-byte plaintext block will always product the same 16-byte ciphertext.