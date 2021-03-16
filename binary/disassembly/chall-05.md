## Challenge 05

Given sequence of byte representing shellcode.

Identify all jump or branching instructions. Map the `address of jump instruction` to `address of destination`. Add a flag to each mapping to indicate whether the path is taken when the condition met.

For example, the code below has one jump instruction:

```
0x00:   jnz     0x4
0x02:   mov     al, 1
0x04:   mov     bl, 1
```

which will produce two tuples:

```
(0x00, 0x04, 1)
(0x00, 0x02, 0)
```

Because `0x00` will jump to `0x04` if condition for `JNZ` is met. Otherwise, `0x00` will jump to `0x02`.

Note: 

- feel free to use any external libraries you want.
- read the file in binary mode.

## Remarks

List of mapping from address to address can be used to make a simple cross reference.