## Challenge 05

Given a sequence of bytes supposed to be a plaintext append with PKCS#7 padding.

Validate if the `PKCS#7` is valid and strips the padding off.

## Test

Assuming the block is 16 byte.

This sequence of bytes is valid `PKCS#7`

```
MII Cybersec\x04\x04\x04\x04
```

while this one is not

```
Pythonidae\x05\x05\x05\x05\x05\x05
```