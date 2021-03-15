## Challenge 06

Given a string `P` as plaintext, a string `K` as key, and a string of 36 characters as `M`.

Encrypt the string with `ADFGVX Cipher` algorithm. Verify the result by decrypting it and compare to the plaintext.

Optionally you can produce a string without uppercase.

## Test

Given a string P and K

```
P = MII Cybersec
K = Xathrya
```

and string M `ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8` which arranged as Polybius square:

```
p h 0 q g 6
4 m e a 1 y
l 2 n o f d
x k r 3 c v
s 5 z w 7 b
j 9 u t i 8
```

should produce

```
DDFGFGVVAXXDXXVDVGVVDF
```

## Remarks

`ADFGVX cipher` is an extension of earlier cipher `ADFGX cipher`. The cipher is a fractionating transposition cipher which combined a modified Polybius square with a single columnar transposition. The name of cipher comes from the six possible letters used in the ciphertext `A`, `D`, `F`, `G`, `V`, and `X`.

The Polybius square is a 6x6 square containing all letters and numbers (a-z, 0-9).

Build the square from `ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8`:

```
    A D F G V X
A | p h 0 q g 6
D | 4 m e a 1 y
F | l 2 n o f d
G | x k r 3 c v
V | s 5 z w 7 b
X | j 9 u t i 8
```

To encipher a message, find the character on the table. Once found, find the row and column. For example, 'C' can be found on row 'G' and column 'V' which result in 'GV'. This will produce `DDXVXVGVDXVXDFGFVADFGV`.

Then Divide the string by length of key. If the key is `xathrya` which have length 7, then this will produce:

```
xathrya
-------
DDXVXVG
VDXVXDF
GFVADFG
V......
```

Sort the column, which gives:

```
aahrtxy
-------
DGVXXDV
DFVXXVD
FGADVGF
.....V.
```

Then write the result column by column.

```
DDF GFG VVA XXD XXV DVGV VDF

DDFGFGVVAXXDXXVDVGVVDF
```