## Challenge 03

Given sequence of byte representing shellcode.

Count all affected registers in instructions and create statistic based on types (source register, destination registers).

Sample expected result:

```
RAX appears 3 times as source, 0 times as destination.
```

If a register never appear on disassembled code, exclude them from list.

Some registers are related. Register such as RAX, EAX, AX, AH, AL have different size but actually aliases for different part of same register. Such registers should be treated as same register instead.

Note: 

- feel free to use any external libraries you want.
- read the file in binary mode.

## Remarks

Identifying registers is useful to track the value of registers in `Data-Flow`, `Taint Analysis`, and other analyses. The goal might be varying, but the common purpose is to know the value of registers at a time.