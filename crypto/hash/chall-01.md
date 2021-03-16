## Challenge 01

Given a string `S` and a salt `G`.

Compute the `MD5` hash value for two possible combination: `md5(G + S)` and `md5(S + G)`.

Note: you are free to use library or implement `MD5` hash algorithm by yourself.

## Test

Given string `S` and `G`

```
S = MII Cybersec
G = xathrya
```

should produces 

```
4e104f3faea572d0f5129bbea63b5a8b
d8109ef05c52c4dda9a69351c4801f86
```

the first line is the value of `md5(G + S)` and the second one is `md5(S + G)`.

## Remarks

Salt is random data used as additional input to hash function. Uniquely generated to each user, either random or following certain pattern. The purpose is to guarantee same message won't produce identic hash value.