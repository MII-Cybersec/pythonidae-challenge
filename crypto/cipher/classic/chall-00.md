## Challenge 00

Given a string `S`. 

Encrypt the string with `ROT13` algorithm. Verify the result by decrypting it and compare to the plaintext.

Optionally, you can produce a string without space and uppercase.

## Test

Given a string `S`

```
MII Cybersec
```

should produce

```
ZVV Plorefrp
```

If the whitespaces are trimmed and all letters become lowercase, then the result would be

```
zvvplorefrp
```

## Remarks

`ROT13` is a classic cipher, a simple letter substitution cipher that replace a letter with 13th letter after it in alphabet. ROT13 is a special case of Caesar Cipher.

The mapping of each alphabet can be seen below:

```
ABCDEFGHIJKLM
NOPQRSTUVWXYZ
```

The shift 13 is chosen because it is a number that divide alphabet to half, making it easier to do encrypting and decrypting.