## Challenge 00

Given a string `S`.

Compute the `MD5` hash value of `S`.

You are free to use library or implement `MD5` hash algorithm by yourself.

## Test

Given string `S`

```
MII Cybersec
```

should produces

```
b56dd2540fce01c955a6b6ea46e75b58
```

## Remarks

`MD5` is a message digest or hash function producing a 128-bit hash value. Initially designed as cryptographic hash function, but later suffer extensive vulnerabilities.

MD5 is widely used as checksum to verify data integrity. It is also used to produce hash value to store sensitive information such as password. However using MD5 to create hash value of password should be avoided.