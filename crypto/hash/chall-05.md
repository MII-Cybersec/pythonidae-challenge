## Challenge 05

Given a string `S` and key `K`.

Compute the hash value using the `HMAC-SHA256`.

## Test

Given string `S` and key `K`

```
S = MII Cybersec
K = xathrya
```

will produce

```
da9e83a4595047e8db5295a3b49e624c23c2000dafd660b91159f1db94de635a
```

## Remarks

`HMAC (Hash-based Message Authentication Code)` is a specific type of `MAC (Message Authentication Code)` involving cryptographic hash function an a secret cryptographic key. HMAC is used to prove the authenticity of the data with a pre-shared key.

HMAC is used for message authenticity, message integrity, and sometimes for key derivation.

HMAC itself is not a hash function. It can use various hash function such as MD5, SHA, HAVAL, etc.