## Challenge 04

Given a binary file `B`, consists of 9 (nine) sections. Each section has the following structure:

```C
struct section_t
{
    uint32_t    length;
    uint8_t     flag;
    uint8_t     name[16];
    uint32_t    pointer;
};
```

where:

- `length`: 4-bytes, is the length or size of used data.
- `flag`: 1-byte, some information for this chunk.
- `name`: 0 to 16 bytes padded with zero, the name of data.
- `pointer`: 4-bytes, address or offset to data.

Read and parse the file. Find out the content of each section by following `section_t.pointer`.

Note:
- all integer value is stored in big-endian format.
- number of section is fix (only 9).

## Test

Use file [sample-03.bin](resources/sample-03.bin).

There are 9 sections.

## Remarks

Data are just sequence of bits, meaningless unless we know how to interpret it.

To store or transmit information efficiently, data should be arranged with certain rules and structure. Sometimes, data should be aligned to certain length or position.

Structured data usually consists of two parts: header and body (payload). Header is a collection of information placed at the beginning of body, such as:

- size of content.
- number and type of subsection available.
- how to interpret data.
- offset to certain parts.

Header might be nested, inside of other headers.