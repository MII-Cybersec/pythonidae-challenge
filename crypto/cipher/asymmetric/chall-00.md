## Challenge 00

Generate public and private key of 4096-bits for RSA with appropriate exponent. Encode and store each key into PEM-format file.

You are free to use library or implement algorithm by yourself.

## Remarks

`RSA (Rivest-Shamir-Adleman)` is a public-key cryptosystem and is widely used for secure data transmission. RSA use a pair of key: `public key` and `private key`. The public key is used to encrypt data which will be sent to system and private key is used by system to decrypt the data.

The RSA strength comes from the difficult of the factorization of the product of two large prime numbers.

`PEM` (Privacy Enhanced Mail) is a Base64-encoded text with start/end delimiters.

Generating RSA public + private key involves following:

- Find three very large integers `e`, `d`, and `n` such that: `(me)d ≡ m (mod n)` for all `m` in the range 0..n
    - `n` is modulus, defines the key length.
- Pair `(n, e)` is public key. 
    - `e` is public key exponent, usually `65537` (0x010001)
- Pair `(n, d)` is private key.
    - `d` is private key exponent.
