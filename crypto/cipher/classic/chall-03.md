## Challenge 03

Given a string `P` as plaintext and string `K` as key.

Encrypt the string with `Rail-Fence Cipher` algorithm. Verify the result by decrypting it and compare to the plaintext.

Optionally, you can produce a string without space and uppercase.

## Test

Given a string `S`

```
MII Cybersec
```

with `R = 3`, should produce

```
McrI yescIbe
```

## Remarks

`Rail-Fence cipher` is a very simple transposition cipher. It split the text into rows and columns and mix the position of character.

The key `R` is the row. The plaintext then write in zig-zag order, alternately moving from top row to bottom row. The ciphertext is produced by read the aligned alphabet row by row.

If we have string `MII Cybersec` and `R = 3`, we then write it as following:

```
M...C...r...
.I. .y.e.s.c
..I...b...e
```

Reading row by row we get `McrI yescIbe`.