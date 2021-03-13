## Challenge 06

Given a string `S` and single-byte `C`.

XOR each character of `S` with `C`. The result bytes might not be printable characters.

Hint: Operate in `bytes` object is recommended.

## Test

The hexpair string

```
526576657273696e672e4944
```

if XOR-ed with 0x53 would give result

```
0136253621203a3d347d1a17
```

## Remarks

XOR is primitive operation that often used to "encrypt" data.

Simple string obfuscation can be implemented with XOR.