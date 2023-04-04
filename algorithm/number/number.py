import math

# Given two integers `A` and `B`.
# Find the `Greatest Common Divisor` between these two.
def chall00(A:int, B:int) -> int:
   return math.gcd(A, B)


# Given an integer `N`. List all of its factors.
def chall01(N:int) -> list:
  idx = 2
  factors = []
  while idx*idx <= N:
    if N % idx == 0:
      factors.append(idx)
      N //= idx
    else:
      idx += 1
  if N > 1:
      factors.append(N)

  return set(factors)


# Given a list of tuple representing a range (Start - End) and an integer I.
# Find out if there is any range which include the integer I.
def chall02(L:list, I:int) -> str:
  for idx in L:
    if idx[0] <= I <= idx[1]:
      return f'Integer {hex(I)} is in the range of ({hex(idx[0])}, {hex(idx[1])})'
  return f'Integer {hex(I)} was not found in any range of tuples'


# MAIN
def main():
  print('### CHALLENGE 00 ###')
  intA_00 = 15
  intB_00 = 27
  print(f'The two ints are A:{intA_00} & B:{intB_00}')
  print(f'The greates common divisor: {chall00(intA_00, intB_00)}')
  print('\n\n')

  print('### CHALLENGE 01 ###')
  intN_01 = 120
  print(f'Integer: {intN_01}')
  print(f'Factors are: {chall01(intN_01)}')
  print('\n\n')

  print('### CHALLENGE 02 ###')
  intI_02 = 0x7f343f010210
  tupleList = [
    (0x00400000, 0x006fa000),
    (0x008f9000, 0x008fa000),
    (0x008fa000, 0x00986000),
    (0x00986000, 0x009a2000),
    (0x021ba000, 0x022a4000),
    (0x7f343d797000, 0x7f343de79000),
    (0x7f343de79000, 0x7f343df7e000),
    (0x7f343df7e000, 0x7f343e17d000),
    (0x7f343e17d000, 0x7f343e17e000),
    (0x7f343f000000, 0x7f343f1b6000),
    (0x7f343f1c5000, 0x7f343f1cc000),
    (0x7f343f1cc000, 0x7f343f1ce000),
    (0x7f343f1ce000, 0x7f343f1cf000),
    (0x7f343f1cf000, 0x7f343f1d0000),
    (0x7f343f1d0000, 0x7f343f1d1000),
    (0x7ffccf1fd000, 0x7ffccf21e000),
    (0x7ffccf23c000, 0x7ffccf23e000),
    (0x7ffccf23e000, 0x7ffccf240000)]
  print(f'Integer as hex: {hex(intI_02)}')
  print(f'List of tuples: {tupleList}')
  print(chall02(tupleList, intI_02))
  print('\n\n')
  
if __name__ == "__main__":
    main()