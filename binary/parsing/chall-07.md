## Challenge 07

Given a path to executable `P` and section name `S`.

Open `P` then add `readable`, `writable`, and `executable` permission to section `S`. Save as new executable.

## Remarks

In executable, section is a container which hold actual data or code. When process is running, access to section is controlled by permission. In most executable format, there are three permission: readable, writable, and executable.

Normally a code section is marked as `readable` and `writable`, thus making execution possible. While `writable` found on section designated as data section.

Marking a section as `writable` grant permission for modifying section, while `executable` make the content can be interpreted as instruction. Usually, this is used for injection shellcode to an executable by finding a codecave inside a section.