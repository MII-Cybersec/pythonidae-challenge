## Challenge 02

Open any executable file (PE / ELF). Print the name, size, and permission of each sections.

You can use any library or parse the executable format manually.

## Remarks

Section is an area on executable file which contain sequence of bytes. The bytes can be interpreted as code or data, depends on the flag. 

The size of section indicates the capacity, maximum amount of bytes it can hold. The actual usage might be less than this size.

Permissions indicate the access rights (read, write, execute) for the section. Once the executable is loaded and mapped by OS, the permission is effectively enforced. Violating the permission (ex: executing the inexecutable section) will raise and exception.