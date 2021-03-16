## Challenge 06

Given a string `S` and key `K`.

Encrypt the string with `AES-128` and `CTR` mode. Encode the result in `Base64` encoding.

You are free to use library or implement `AES` algorithm by yourself.

## Remarks

`CTR (counter)` is an encryption mode where encryption is done against a running counter instead of plaintext. This will produce block of keystream which is XORed against the plaintext.

Modern cryptography relies on `CTR` mode to adapt block ciphers into stream ciphers. 