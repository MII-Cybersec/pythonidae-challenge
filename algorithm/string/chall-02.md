## Challenge 02

Given a string `D` and two integers `S` and `E`.

Rewrite the content of string, starts from index `S` to index `E`, fill with `x`. The resulting string and `D` should have same length.

Also, try the same thing with `bytes` type.

## Test

Given a string `D`

```
MII CyberSec Consulting Service
```

and two integers `S = 4` and `E = 11`.

the result should be

```
MII xxxxxxxx Consulting Service
```

## Remarks

Index is a number to refer position of specific element.

String `str` and `bytes` are both immutable and do not support item assignment on their element.

Modify a string at certain range is not limited to masking. We can modify content of (structured) packets, and create a rule: where and what to replace.