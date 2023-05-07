from math import ceil
import random


# Given a list of integer `L`. Get the largest number from the list.
# There is no guarantee that the list is in ordered (sorted) condition.
# If the largest number appear multiple time, return them all.
def chall00(L:list) -> list:
  return [max(L)] * L.count(max(L))

# Given a list of integer `L`. Multiplies all items with 3.
def chall01(L:list) -> list:
   return [item * 3 for item in L]


def chall02(L:list) -> int:
  return sum(L[1::2]) 


def chall03(L:list) -> list:
   return sorted(L, key=len)


def chall04(L:list) -> list:
   return [*set(L)]


def chall05(L:list) -> list:
   return [item for item in L if L.count(item)==1]


def chall06(L:list, opt:str) -> tuple:
   randSelect = random.choice(L)
   L.remove(randSelect) if opt=='discard' else None
   return (randSelect, L)


def chall07(L:list) -> list:
   random.shuffle(L)
   return L


def chall08(L:list) -> list:
   return [item for sublist in L for item in sublist]


def chall09(S:int, E:int) -> list:
   L = [x for x in range(S,E+1)]
   random.shuffle(L)
   return(L)


def chall10(S:str) -> list:
   return [ord(x) for x in S]


def chall11(L:list, M:list) -> list:
  return [*set(L).intersection(set(M))]


def chall12(L:list, M:list) -> list:
   return list(zip(L,M))


def chall13(L:list, N:int) -> list:
   return [L[x:x+N] for x in range(0, len(L), N)]


def chall14(L:list, N:int) -> list:
   s = ceil(len(L)/N)
   return [L[x:x+s] for x in range(0, len(L), s)]


def chall15(N:int, K:int) -> list:
   return [x for x in range(N) if x%K != 0]


def chall16(L:str) -> list:
   foo = L.strip(' []').split(',')
   bar = [[y for y in range(int(x[0]),int(x[x.find('-')+1:])+1)] if '-' in x else [int(x)] for x in foo]
   return [item for sublist in bar for item in sublist]


# MAIN
def main():
  print('### CHALLENGE 00 ###')
  L_00 = [ 4, 5, 3000, 1, 6, 7, 3000, 2, 8, 9, 1, 6, 9, 3000 ]
  print(f'Old list: {L_00}')
  print(f'New list: {chall00(L_00)}')
  print('\n\n')

  print('### CHALLENGE 01 ###')
  L_01 = [ 1, 6, 7, 2, 8, 1000 ]
  print(f'Old list: {L_01}')
  print(f'New list: {chall01(L_01)}')
  print('\n\n')

  print('### CHALLENGE 02 ###')
  L_02 = [ 3, 0, 4, 9, 7, 9, 7, 2, 9, 4, 1, 4, 2, 5, 5, 7, 4, 0, 6, 9 ]
  print(f'Old list: {L_02}')
  print(f'New list: {chall02(L_02)}')
  print('\n\n')

  print('### CHALLENGE 03 ###')
  L_03 = ['MII-CyberSec', 'Xathrya', 'Reversing.ID', "devin"]
  print(f'Old list: {L_03}')
  print(f'New list: {chall03(L_03)}')
  print('\n\n')

  print('### CHALLENGE 04 ###')
  L_04 = [ 1, 1, 2, 3, 4, 4, 6, 9 ]
  print(f'Old list: {L_04}')
  print(f'New list: {chall04(L_04)}')
  print('\n\n')

  print('### CHALLENGE 05 ###')
  L_05 = [ 1, 1, 2, 3, 4, 4, 6, 9 ]
  print(f'Old list: {L_05}')
  print(f'New list: {chall05(L_05)}')
  print('\n\n')

  print('### CHALLENGE 06 ###')
  L_06 = ['Devin', 'Charles', 'Tana', 'Bella']
  print(f'Old list: {L_06}')
  print(f'New list (keep): {chall06(L_06, "keep")}')
  print(f'New list (discard): {chall06(L_06, "discard")}')
  print('\n\n')

  print('### CHALLENGE 07 ###')
  L_07 = [ 3, 2, 6, 7, 2 ]
  print(f'Old list: {L_07}')
  print(f'New list: {chall07(L_07)}')
  print('\n\n')

  print('### CHALLENGE 08 ###')
  L_08 = [ [2, 4, 3], [1, 5, 6], [9], [7, 9] ]
  print(f'Old list: {L_08}')
  print(f'New list: {chall08(L_08)}')
  print('\n\n')

  print('### CHALLENGE 09 ###')
  S_09 = 3
  E_09 = 100
  print(f'New list: {chall09(S_09, E_09)}')
  print('\n\n')

  print('### CHALLENGE 10 ###')
  S_10 = 'Devin'
  print(f'New list: {chall10(S_10)}')
  print('\n\n')

  print('### CHALLENGE 11 ###')
  L_11 = [ 1, 2, 3, 4, 5, 6, 7 ]
  M_11 = [ 2, 6, 10, 12 ]
  print(f'New list: {chall11(L_11, M_11)}')
  print('\n\n')

  print('### CHALLENGE 12 ###')
  L_12 = [ 1, 3, 5, 7, 9 ]
  M_12 = [ 2, 4, 6, 7 ]
  print(f'New list: {chall12(L_12, M_12)}')
  print('\n\n')

  print('### CHALLENGE 13 ###')
  L_13 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]
  N_13 = 4
  print(f'New list: {chall13(L_13, N_13)}')
  print('\n\n')

  print('### CHALLENGE 14 ###')
  L_14 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]
  N_14 = 6
  print(f'New list: {chall14(L_14, N_14)}')
  print('\n\n')

  print('### CHALLENGE 15 ###')
  N_15 = 15
  K_15 = 3
  print(f'New list: {chall15(N_15, K_15)}')
  print('\n\n')

  print('### CHALLENGE 16 ###')
  L_16 = '[1,               3,5-50, 100, 101, 3000]'
  print(chall16(L_16))
  print('\n\n')
  
if __name__ == "__main__":
    main()