## Challenge 02

Given a string `S` and key `K`.

Encrypt the string with `3DES` and `ECB` mode. Encode the result in `Base64` encoding.

Note: you are free to use library or implement `3DES` algorithm by yourself.

## Remarks

`Triple DES (3DES, TDES)` is an extension to `DES` which applying `DES` encryption three times to each data block. Therefore, instead of using one key `3DES` use three different keys.

Usually the encryption algorithm is:

```
ciphertext = Ek3(Dk2(Ek1(plaintext)))
```

while the decryption is:

```
plaintext = Dk1(Ek2(Dk3(ciphertext)))
```