## Challenge 04

Given a string `S` and key `K`

Encrypt the string with `AES-128` and `CBC` mode. Encode the result in `base64` encoding.

You are free to use library or implement `AES` algorithm by yourself.

## Remarks

`CBC (Cipher Block Chaining)` is an encryption mode where the plaintext block is XORed with previous ciphertext block before being encrypted. This way each ciphertext block depends on the all plaintext blocks processed up to that point. 

When encrypting the first block, a special block dubbed as `IV (Initialization Vector)` is used to replace the previous ciphertext block.