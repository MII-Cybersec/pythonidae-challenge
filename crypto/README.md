# Pythonidae Challenge

Learn Python for Cyber Security by completing challenges.

#### Crypto

This is `Crypto Set`. This set is suitable for you to learn cryptography in Cyber Security context.

The goal of cryptography is to securely sharing secrets with others so no adversaries can learn the secret.

## Table of Content

You will see

- `Encoding`
- `Cipher` (Classic, Block, Stream, Asymmetric)

#### Encode

Encoding is conversion of data from one form to other form. Usually reduce loss in transmission or represent data in readable format.

0. base64.
1. base85.
2. url.
3. uu encoding.
4. xx encoding.

#### Cipher
    
classic

0. ROT13
1. Atbash
2. Affine
3. Rail-Fence
4. Vigenere
5. Beaufort
6. ADFGVX
7. Playfair

block

0.  generate random bytes for key
1.  DES
2.  3DES
3.  AES/ECB
4.  AES/CBC
5.  validate PKCS#7 and strip
6.  AES/CTR
7.  Camellia

stream

0. Salsa20

asymmetric

0. generate RSA key-pair and store in PEM.
1. generate RSA key-pair and store in PEM protected by passphrase.
2. read the public key from PEM file and do RSA encryption.
3. read the private key from PEM file and do RSA decryption.
4. generate ECC key-pair and store in PEM protected by passphrase.
5. read the private key from PEM file and do ECC encryption.
6. read the public key from PEM file and do ECC decryption.