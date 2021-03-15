## Challenge 02

Given a string `S` and two integers `A` and `B`.

Encrypt the string with `Affine Cipher` algorithm. Verify the result by decrypting it and compare to the plaintext.

Optionally, you can produce a string without space and uppercase.

## Test

Given a string `S`

```
MII Cybersec
```

with `A = 5` and `B = 9`, should produce

```
RXX Tzodqvdt
```

## Remarks

`Affine Cipher` is a substitution cipher which requires two integers as key. It uses mathematic equation to generate the substituting character.

The encryption algorithm has following equation

```
C = (A * P + B) mod M

1 <= A <= M
1 <= B <= M 
```

And the decryption algorithm 

```
P = A^(-1) * (C - B) mod M
```

Not all number can be used. The value of `M` is 26 or the space of possible alphabet. `A` and `B` should be relatively prime to `M` (`A` and `B` have no factors in common with `M`). Thus, the possible range of value: 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25