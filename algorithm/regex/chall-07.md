## Challenge 07

Shadow file is a colon delimited file with 2nd field contain the password information. The password is encoded using the following format:

- consists of 3 parts delimited by dollar sign.
- first part indicate cipher algorithm.
- second part indicate salt
- third part indicate password hash.

Given an such entry, retrieve each field.