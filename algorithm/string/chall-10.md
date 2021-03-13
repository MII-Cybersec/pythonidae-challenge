## Challenge 10

Given a string `S` and list of integer `P`, both have the same length `N`. Each element of list `P` is a unique number which value is in range `0` to `N-1`.

Create a new string `T`, which is permutation of `S` using `P` as index.

## Test

Given the string `S`

```
MII-CyberSec
```

and the list of integer `P`

```
[4, 0, 9, 5, 6, 10, 2, 8, 1, 7, 3, 11]
```

will produce a new string

```
CMSybeIrIe-c
```

See that the list `P` at index 0 has value 4. If we look at the string `S`, we note that the character at index 4 is "C". Thus, "C" will be the character at index 0 of the string `T`.

## Remarks

Permutation of string is one of operation in classic cipher. Even some operation in block cipher has permutation.

Permutation of string is one of operation in classic cipher. Permutation is also used as operation in block cipher, such as `Substitution-Permutation Network (SPN)`, where bits of plaintext is rearranged according a rule (Permutation Box).