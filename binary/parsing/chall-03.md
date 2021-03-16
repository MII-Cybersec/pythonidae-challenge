## Challenge 03

Open any executable file (PE / ELF). List all function with its address, registered at import section.

You can use any library or parse the executable format manually.

## Remarks

Import section is a section where executable will use functions from foreign object (executable or shared library). Shared libraries can be third party libraries or OS-provided libraries. Analyzing import libraries in some case can gain understanding of what executable will do.