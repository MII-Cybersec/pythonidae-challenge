## Challenge 04

Generate public and private key or ECC with appropriate curve parameter. Encode and store each key into PEM-format file and protected by passphrase.

You are free to use library or implement algorithm by yourself.

## Remarks

`ECC` (Elliptic Curve Cryptography) is modern family of public-key cryptosystem, which is based on the algebraic structures of the elliptic curves over finite field and on the difficulty of th Elliptic Curve Discrete Logarithm Problem (ECDLP).

ECC implements all major capabilities of the asymmetric cryptosystems: encryption/decryption, signatures, and key exchange.

Compared to RSA, ECC use smaller keys for the same level of security and provides fast key generation, fast key agreement, and fast signatures.

`PEM` (Privacy Enhanced Mail) is a Base64-encoded text with start/end delimiters.

The private keys in the ECC are integers (in the range of the curve's field size). The public keys in the ECC are EC points, pairs of integers coordinate {x, y} laying on the curve.