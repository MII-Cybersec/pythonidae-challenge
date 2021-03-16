## Challenge 00

Load functions from shared libraries (DLL / SO) based on name.

## Test 

If you are in Windows, load the [clib-64.dll](clib-64.dll) (for Python x64) or [clib-32.dll](clib-32.dll) (for Python x86) and then execute function `hello`.

If you are in Linux, load the [clib-64.so](clib-64.so) (for Python x64) or [clib-32.so](clib-32.so) (for Python x86) and then execute function `hello`.

## Remarks

Some tools are implement as shared libraries and exported their functions to public. By loading the shared library, Python can call the functions directly.