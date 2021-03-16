## Challenge 04

Given a string `S` and integer `R`.

Compute the `bcrypt` hash value for R rounds.

You are free to use library or implement bcrypt hash algorithm by yourself.

Note: two digest produced by `bcrypt` for same string might be different. However both are valid when verified.

## Test

Given string `S` and integer `R`

```
S = MII Cybersec
R = 12
```

might produce

```
$2y$12$w.AGyPlNPuAv9n3agPG65.M6974EZcyYkWxNxecaV4elttFNC.oSu
```

## Remarks

The `bcrypt (blowfish-based crypt)` algorithm is a specific type of `KDF (Key Derivation Function)` which is used to create a key from user password.

`Bcrypt` is specialized in password hashing function. This algorithm is a modification of `Blowfish cipher` as hash function.

By design, this function require a salt to protect against rainbow table attack. The interesting thing about bcrypt is the adaptive function, which over time, the iteration count can be increased to make it slower. Therefore it remains resistant to brute-force search attacks even with increasing computation power.

The bcrypt function is the default password hash function algorithm for OpenBSD and some Linux.