## Challenge 02

Given a string `S`.

Encode it with `URL encoding`. Verify te result by decoding it back and compare to original value.

You are free to use library or implement URL encoder/decoder by yourself.

## Test

Given string `S`

```
MII Cybersec
```

should produce

```
MII+Cybersec
```

## Remarks

`URL encoding` is commonly used in web technologies. It is used to represent some characters to avoid ambiguity. When dealing with URLs (and the body of POST request), they can only contain printable ASCII characters (codes between 32 and 126 or 0x20 - 0x7E). Some characters within this range has special meaning within the URL or within HTTP protocol. 

In general, `URL Encoding` might transform single character to their hex equivalent in the format `%XX` where XX is the hexpair.

```
% -> %25
space -> %20
tab -> %09
= -> %3D
```

Note that, on URL you can also represent a space using +.