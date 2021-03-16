## Challenge 02

Given a string `S`, and two integer `M` and `N`.

The string `S`, with size `M`, had been encrypted by a string `K` of size `N`.

Find the `K`.

## Test

Given a string `S` (length = 36)

```
281800001d17081c001148111100140d1106151c411a1854253b304c3b18160d002a041b
```

and `N` = 7.

the key should be: `78617468727961` (length = 7)

## Remarks

XOR operation is still commonly used as fast encryption algorithm.

One way to break this is to guessing the key length and find the edit distance between each block. 

General idea would be like this:

1. let `KEYSIZE` be the guess length of the key, which range from `2` to `N-1`
2. divide the string `S` into blocks of `KEYSIZE` data
3. compute the edit distance of a block with next block and then normalize this result by dividing by `KEYSIZE`.
4. the `KEYSIZE` with smallest normalized edit distance is probably the key.
5. after guessing the `KEYSIZE`, transpose the block, make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
6. solve each block as if it was single-character XOR.
7. single-byte XOR key that produce the best looking histogram is the repeating XOR key byte for that block. Putting them together and you get the key.