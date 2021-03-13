## Challenge 03

Given three integers: `N`, `S`, `E`.

Create a bytearray `B` with the length `N`. Fill `B` from index `S` to `E` with random byte . `N` is guaranteed to be no less than `E`.

## Test

Given three integers: `N = 10`, `S = 5`, `E = 8`.

one of possible output would be:

```
bytearray(b'\x00\x00\x00\x00\x00\x0B\xAD\xF0\x0D\x00')
```

## Remarks

The `bytearray` object is a mutable object consists of sequence of bytes. Bytearray is usually used as a buffer to support in-place modification of data.

The `bytes` object and `bytearray` are usually complementing.

Mutable buffer often needed to build a payload, which some parts will be modified later by other function.