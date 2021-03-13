## Challenge 05

Given a string of a hexpair `H`.

Decode (or convert) `H` as a sequence of bytes. The content might or might not be printable characters.

The length of `H` is guaranteed to be even.

## Test

The hexpair string `H` (length = 24)

```
526576657273696e672e4944
```

should be converted to (length = 12)

```
\x52\x65\x76\x65\x72\x73\x69\x6e\x67\x2e\x49\x44
```

## Remarks

Representing binary data in hexpair string is not unusual. Although some encoding such as Base64 is more popular. Hex pairs are often found on low level stuffs for representing stream of data.