## Challenge 05

Given a binary file `B` and integer `I`.

`B` consists of multiple indexes. Each index has following structure:

```C
struct index_t
{
    uint32_t    key;
    uint32_t    pointer;
};
```

where:

- `key`: 4-bytes, integer which identify specific entry of data.
- `pointer`: 4-bytes, address or offset to collection of data.

Read and parse the file. Find out the block pointed by index which might hold the key `I`.

Note:
- all integer value is stored in big-endian format.
- number of chunks is limited by file size.

## Test

Use file [sample-04.bin](resources/sample-04.bin).

## Remarks

To efficiently store large volume data, structured data are kept ordered. Ordering data by key making search and data retrieval faster. The strategy is to skip several blocks of entries until specific key is found (or not). Key is a field which designated as pivot.

Entries are divided into several blocks. Each block contain some entries. All relatively ordered by the key.

To help searching operation, index is built and maintained. Index is populated as array. Each index will point to the first entry of a block. Thus, iterating index means iterating blocks, which in turns skipping several entries.

With indexing, searching operation would first find the correct block which would contain our entry. If a block is found, a search is done sequentially to find the correct entry.

Usually, indexes are kept as separate file. In some case, index can be multilayer.