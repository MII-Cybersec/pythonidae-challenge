## Challenge 02

Given a string `S` and path to PEM file for public key.

Read the PEM-file and encrypt the string `S` using RSA with OAEP padding. Encode the result in `base64` encoding.

You are free to use library or implement RSA algorithm by yourself.

## Remarks

Compared to symmetric block cipher, RSA ran slower and might not be suitable to encrypt large data in real time. In practice, RSA is used in initial stage to establish a connection between the parties. RSA commonly used to encrypt symmetric key. This symmetric key as well as the agreed block cipher then used to communicate.

Encrypting message using RSA public key `(n, e)` is done by following transformation:

```
c = p.e mod n
```

`p (plaintext)` is encoded as integer in the range [0..n). 