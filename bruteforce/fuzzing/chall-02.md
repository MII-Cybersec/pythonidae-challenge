## Challenge 02

Given a large string `S` and an integer `R` in the range `1 to 100`.

The integer `R` represent the ratio of random characters and unchanged characters as percentage.

Do the following until the ratio reach `R`.

- Choose a random number `O` which in the range `1 to 10`
- Advance to next `O` characters from current position (initially start of string). If it past the last character, then stop.
- Change whatever character on current position to random byte.

Once done, compute the ratio of random characters and unchanged characters.

## Remarks

`Fuzzing` is mutating (changing) a portion of string to random character and feed it as input to process.

Mutation can be done in random position for certain amount of characters. 