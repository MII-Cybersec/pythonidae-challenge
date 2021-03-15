## Challenge 00

Given a string `S`.

Encode it with `Base64`. Verify te result by decoding it back and compare to original value.

You are free to use library or implement `Base64` encoder/decoder by yourself.

## Test

Given string `S`

```
MII Cybersec
```

should produce

```
TUlJIEN5YmVyc2Vj
```

## Remarks

`Base64` is one of common encoding used in many cases. It is used to represent binary data. Some common usages:

- encode user credentials in basic HTTP authentication
- encode email attachments for transmission over SMTP
- transmit encrypted request/response body.

`Base64` looks data in blocks of 3 bytes (24-bits). These 24 bits are then divided into 4 chunks of 6-bits each. Each chunks is then mapped to the corresponding `Base64` values (on a table). 

`Base64` use 64 different printable characters: a-z, A-Z, 0-9, +, / and padding =.

Other encoding on same family: `Base32`, `Base16`, `Base85` (or `Ascii85`).