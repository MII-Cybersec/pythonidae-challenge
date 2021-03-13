## Challenge 02

Given a list of tuple representing a range (Start - End) and an integer `I`.

Find out if there is any range which include the integer `I`.

## Test

Given a list of tuple

```
(0x00400000, 0x006fa000)
(0x008f9000, 0x008fa000)
(0x008fa000, 0x00986000)
(0x00986000, 0x009a2000)
(0x021ba000, 0x022a4000)
(0x7f343d797000, 0x7f343de79000)
(0x7f343de79000, 0x7f343df7e000)
(0x7f343df7e000, 0x7f343e17d000)
(0x7f343e17d000, 0x7f343e17e000)
(0x7f343f000000, 0x7f343f1b6000)
(0x7f343f1c5000, 0x7f343f1cc000)
(0x7f343f1cc000, 0x7f343f1ce000)
(0x7f343f1ce000, 0x7f343f1cf000)
(0x7f343f1cf000, 0x7f343f1d0000)
(0x7f343f1d0000, 0x7f343f1d1000)
(0x7ffccf1fd000, 0x7ffccf21e000)
(0x7ffccf23c000, 0x7ffccf23e000)
(0x7ffccf23e000, 0x7ffccf240000)
```

an integer `0x7f343f010210` is in the range of `(0x7f343f000000, 0x7f343f1b6000)`. 

## Remarks

Section of executable binary will be mapped to a memory region at load time. Sometimes, we need to locate the memory region which an address belong to.