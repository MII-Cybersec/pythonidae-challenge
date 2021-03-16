## Challenge 03

Given a base64-encoded string `S` and path to PEM file for private key.

Read the PEM-file and decrypt the decoded string `S` using RSA with OAEP padding.

You are free to use library or implement RSA algorithm by yourself.

## Remarks

Decrypting message using RSA private key `(n, d)` is done by following transformation:

```
p = c.d mod n
```

`c (ciphertext)` is encoded as integer in the range [0..n). 