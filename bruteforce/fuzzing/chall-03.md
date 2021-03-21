## Challenge 03

Given a string `G` as grammar.


The grammar consists of two parts: static and dynamic. Static part is immutable (cannot change) during operation, while dynamic part is mutable. Fuzzing only done on parts which marked as mutable.

The grammar applied:

- Alphabet can be letter (lowercase/uppercase), number, whitespaces, or special symbol.
- static or immutable string is enclosed by `()`.
- dynamic or mutable string is marked as `\f`.
- if mutable string only valid for certain set alphabet, defined by enclosing with `[]`.
- If symbol such as `{`,`}`,`\` will be used as alphabet, add `\` in front of them.

Generate fuzzing payload which follow rules of `G`.

## Test

Given a string `G`

```
(USER) \f
```

should give some payloads:

```
USER a
```

## Remarks

Protocol such as `HTTP`, `FTP`, etc defined strict standard of how it can communicate. Fuzzing for protocol should follow the standard. For this purpose, fuzzer should know which part is mutable and immutable. Some immutable parts can be command and flags.