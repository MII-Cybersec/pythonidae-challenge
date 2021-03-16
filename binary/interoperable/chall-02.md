## Challenge 02

Call function `modify_str` in given shared library, pass a mutable string as argument. Print the string after call.

Note: the string should be different.

## Test 

Based on your architecture, load the `clib` shared library. Call `modify_str` and pass a string.

Each element of the string should shift to next alphabet.

## Remarks

Python string is immutable, the string on low level might be not. When interacting with low level code, a mutable buffer should be used.