## Challenge 00 

Given a string `S` and integer `N`.

Divide the text into block of `N` character(s) and count the appearance of each block in the text.

If `S` is not multiple of `N`, add padding at the end.

## Test

Given a string 

```
MII Cybersec
```

and `N = 2`

will produce result:

```
{
    "MI": 1,
    "I ": 1,
    "Cy": 1,
    "be": 1,
    "rs": 1.
    "ec": 1
}
```

## Remarks

Frequency counting create a statistic of individual character and how often it appears on text. Statistic then can be used to map most frequent character in language of reference.

Often, it is desirable to look not at how often characters appear but at what characters they appear next to. N-gram (digram for 2, trigram for 3, etc) create statistic of how often characters appear.