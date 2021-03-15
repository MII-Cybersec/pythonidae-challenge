## Challenge 07

Given a pstring `P` as plaintext and string `K` as key.

Encrypt the string with `Playfair Cipher` algorithm. Verify the result by decrypting it and compare to the plaintext.

This algorithm require no whitespace.

Optionally you can produce a string without uppercase.

## Test

Given a string P and K

```
P = MII Cybersec
K = xathrya
```

should produce

```
OFFVYDZAOCFY
```

## Remarks

`Playfair Cipher` is a digraph substitution cipher, encrypting pairs of letters (digraphs) instead of single letters. This algorithm use key-square which built based on the key. The size of square is `5x5`.

Building the square take only unique alphabet from the key. Thus, key `xathrya` would be `xathry`. Then append other remaining alphabet which do not appear yet. The `I` and `J` are considered as same value. Which, the square for key `xathrya` would be:

```
x a t h r
y b c d e
f g i k l
m n o p q
s u v w z
```

Any sequence of 25 letters can be used as the key, as long as all letters are in and there are no repeats.

For each digraph, locate the position of each character. Encryption process follow the rules below:

- if both letters appear on the same row, replace with the letters to their immediate right.
- if both letters appear on the same column, replace with the letters to their immediate below.
- if the letters form a rectangle, replace with the letters on the same row but at the other pair of corners of the rectangle.

For example the digraph 'MI' will create a rectangle 'MOIF', which makes the 'OF' as ciphertext.