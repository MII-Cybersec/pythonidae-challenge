## Challenge 00

Given integer `N`.

Generate list of string with length exactly `N`. Each element of string is lowercase alphabet (a-z).

Save the list as file with each line contain only a string.

## Test

Given `N = 2`, should produce `[ aa, ab, ac, ... , zy, zz ]`

## Remarks

Brute force is an attempt to try all possibilities of states to crack verification system. The attack is based on trial and error. The heart of this attack is wordlist, a large amount of words that will be verified one by one.

Larger wordlist will raise the chance of success but would require longer time. Therefore, creating a correct wordlist is essentially useful.

One approach is to create all words from all possible characters on certain length. This require large space to store the result.