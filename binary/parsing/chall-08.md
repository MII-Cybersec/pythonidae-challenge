## Challenge 08

Open any executable file (PE / ELF).

List all sections which have empty space at the end of section. The empty space is defined as gap between `physical` and `virtual` address of section's end.

For each gap found, give the virtual address and size.

Optionally, you can filter code cave by the size.

## Remarks

Finding code cave.

A code cave is a series of unused byte in process memory. In offensive operation, this area is usually injected with custom instruction which then executed at runtime.

A section is allocated as multiple of pages. Therefore, the start address and the size is physically set as multiple of pages. The actual size of content (code/data) however are not always have same size. Thus, the virtual size reflected the actual size which is mostly less than the physical size.