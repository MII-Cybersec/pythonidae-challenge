## Challenge 00

Given a large string `S`.

Do the following until reaching end of string.

- Choose a random number `O` which in the range `1 to 10`
- Advance to next `O` characters from current position (initially start of string). If it past the last character, then stop.
- Change whatever character on current position to random byte.

Once done, compute the ratio of random characters and unchanged characters.

## Remarks

`Fuzzing` is mutating (changing) a portion of string to random character and feed it as input to process.

Mutation can be done in random position for certain amount of characters.