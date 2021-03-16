## Challenge 01

Given a string `S` which had been encrypted by a single-character XOR.

Find the key.

## Test

Given a string `S` (in hexpair representation)

```
d7fef3efe8e9eee3e6e2a7e4efe6ebebe2e9e0e2a7e5fea7caceceaac4fee5e2f5d4e2e4
```

should have key `0x87`

## Remarks

XOR operation is still commonly used as fast encryption algorithm.

One way to break this is to measure how much probability of it resemble a valid string.

If the string is a valid message in certain language (i.e: English), then counting letter frequency might help. Find out the most common letter and map it to most common letter in that language.