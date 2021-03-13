## Challenge 14

Given a list `L` and integer `N`.

Split list into `N` partitions. 

If the size of `L` is not multiple of `N`, some blocks might have less member than the rest.

## Test

Given a list `L` (length = 14)

```
[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]
```

using `N = 3`, it will produce

```
[ ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n'] ]
```

the first and second partition (block) has 5 members while the last block has 4.

## Remarks

Partitioning or splitting the list into several blocks of equal length.

Partitioning is useful to divide the load so we can distribute it into several workers and executed concurrently.