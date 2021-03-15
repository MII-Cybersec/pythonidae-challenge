## Challenge 04

Given a string `S`.

Encode it with `XX encoding`. Verify te result by decoding it back and compare to original value.

You are free to use library or implement XX encoder/decoder by yourself.

## Test

Given string `S`

```
MII Cybersec
```

should produce

```
begin 644 input.txt\nAHIZ762BtMaJmQqJX\nend\n
```

## Remarks

The `xxencoding` is used to represent binary data and use similar format to uuencoding. It only uses alphanumeric characters, the plus, and minus signs.