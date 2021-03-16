## Challenge 05

Open any executable file (PE / ELF). Given an integer `N`, list all printable string which has length no less than `N`. 

Optionally, you can:

- accept a address range, in which searching will be conducted.
- limit the searching to only data section.
- accept a custom function to filter the string.

## Remarks

Strings can be used as initial analysis. They can be messages which appears on specific events. They can be some hardcoded information used for undocumented processes. Some strings can also be used as reference to functions or code segment that is loaded manually.

When dealing with interesting strings, one can try to do cross-reference and find any code which use the string.