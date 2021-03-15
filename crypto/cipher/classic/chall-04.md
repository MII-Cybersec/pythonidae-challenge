## Challenge 04

Given a string `P` as plaintext and string `K` as key.

Encrypt the string with `Vigenere Cipher` algorithm. Verify the result by decrypting it and compare to the plaintext.

Optionally you can produce a string without uppercase.

## Test

Given a string P and K

```
P = MII Cybersec
L = Xathrya
```

should produce

```
JIBJpzeosxj
```

## Remarks

`Vigenere cipher` is a popular cipher polyalphabetic substitution cipher. The method was originally described by `Giovan Battista Bellaso` but misattributed to `Blaise de Vigenere`. Blaise de Vigenere actually create another cipher known as Autokey cipher.

The encryption and decryption method use a table of characters. It use following tabula recta.

```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    ---------------------------------------------------
A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

The top row is the alphabet for the key, and the first column is the alphabet for plaintext. To encipher a message, repeat the keyword above the plaintext

```
XathryaMIIC
MIICybersec
```

First, find the row of plaintext `M`. Then find the column of key `X`. The row `M` and column `X` is intersected to `J` so `J` is the ciphertext.

`Autokey` and `Vigenere` cipher differs in how they positioning the plaintext and key in the table.