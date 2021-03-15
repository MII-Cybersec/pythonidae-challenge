## Challenge 05

Given a regex-like string `R`.

Generate a word following the rules of `R`.

`R` is a finite set of characters. Every alphabet of `R` indicate a single character of result word. The following rules are applied:

- Alphabet can be letter (lowercase/uppercase), number, or special symbol.
- The `[ ]` operator is used for alternative alphabet.
    * each alphabet inside is alternative of a single character on that position. For example `a[abc]` will produce 3 words: `aa, ab, ac`.
    * range of alphabet is specified by `-`. For example `3[a-d]` will produce 4 words: `3a, 3b, 3c, 3d`.
    * more complex range is possible. For example `c[a-b0-3]` will produce 8 words: `ca0, ca1, ca2, ca3, cb0, cb1, cb2, cb3`.
- The `{ }` operator is used for repetition for alphabet or group.
    * `{N}` means the alphabet or group will repeat `N` times. The `a{2}` will produce `aa` but `[ab]{2}` will produce `aa, ab, ba, bb`.
    * `{L,M}` means the alphabet or group will repeat at least `L` times and at most `M` times. The `a{2,3}` will produce `aa, aaa`, while `[ab]{2,3}` will produce `aa, bb, aaa, bbb`.
- If symbol such as `[`, `]`, `{`, `}`, `\` will be used as alphabet, add `\` in front of them.
- escape characters exist to represent a group of alphabet.
    * `\u` for uppercase, has same effect as `[A-Z]`
    * `\l` for lowercase, has same effect as `[a-z]`
    * `\s` for lowercase + uppercase, has same effect as `[a-zA-Z]`
    * `\d` for numerical digit, has same effect as `[0-9]` 

## Test

Given a string `R`

```
p[aA@4]ssword\d{0,2}
```

should produce

```
password
pAssword
p@ssword
p4ssword
password1, password2, ... , password9
pAssword1, pAssword2, ... , pAssword9
p@ssword1, p@ssword2, ... , p@ssword9
p4ssword1, p4ssword2, ... , p4ssword9
password11, password12, ... , password99
pAssword11, pAssword12, ... , pAssword99
p@ssword11, p@ssword12, ... , p@ssword99
p4ssword11, p4ssword12, ... , p4ssword99
```

with total of 4000 words.

## Remarks

Instead of writing new script for each pattern, we can create a language to quickly generate a wordlist. With this approach, we only create a regex pattern to create a worldlist.