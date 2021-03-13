## Challenge 08

Given two unequal-length hexpair string, `S1` and `S2`, with `S1` always longer than `S2`.

XOR `S1` and `S2`.

Also, try to handle when `S1` is shorter than `S2`.

Hint: Operate in `bytes` object is recommended.

## Test

Given a string `S1`

```
d5577f20f541602be01c4001
```

when XORed with another string `S2`

```
87320945
```

will produce

```
526576657273696e672e4944
```

As seen, `S2` is shorter. When iteration came to the end of `S2`, the operation is resumed from the beginning of `S2`. Thus

```
d5577f20 f541602b e01c4001
87320945 87320945 87320945
-------------------------- xor
52657665 7273696e 672e4944
```

## Remarks

XOR is primitive operation that often used to `encrypt` data.

Simple string obfuscation can be implemented with XOR.

The "key" for XOR-ing usually a multi-byte integer. For simple calculation, it often represented in size of word or multiple of it.