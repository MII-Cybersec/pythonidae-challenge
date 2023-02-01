from random import randbytes, randint
from binascii import unhexlify


# Given a string S, convert S to a sequence of bytes object and get its length
def chall00(S: str) -> int:
  # Create byte object with encoding 'utf-8'
  bytesString = bytes(S, 'utf-8', errors='ignore')
  # Return the lenght of the byte array
  return (len(bytesString))
  

# Given a string U and a list of strings E, create a new list by concatenating each 
# element of E with U
def chall01(U: str, E: list) -> list:
  newList = []
  for idx in E:
    newList.append(f'{U}{idx}')
  return newList


# Given a string D, and two ints S & E. Rewirete the string between index S to E to
# replace with `x`
def chall02(D: str, S: int, E: int) -> str:
  newStr = ''
  for idx in range(len(D)):
    if S <= idx <= E:
      newStr += 'x'
    else:
      newStr += D[idx] 
  return newStr


# Given three ints: N, S, E. Create a bytearray B with the length N, fill B with 
# random bytes between indexes S to E  
def chall03(N:int, S:int, E:int) -> bytearray:
  bList = []
  for idx in range(N):
    if S <= idx <= E:
      bList.append(randint(0,127))
    else:
      bList.append(0)
  print(bList)
  return bytearray(bList)


# Given a long string S, Find and extract all substring starts with http:// or 
# https://. The substring should have no whitespace.
def chall04(S:str) -> list:
  stringToAppend = []
  validHttpFormats = ['http://', 'https://']
  splitString = S.lower().split()
  for idx in splitString:
    for jdx in validHttpFormats:
      if jdx in idx:
        stringToAppend.append(idx[idx.index(jdx):])
  return stringToAppend


# Given a string of a hexpair H, Decode (or convert) H as a sequence of bytes. 
# The content might or might not be printable characters.
def chall05(H:str) -> bytearray:
  splitSize = 2
  splitString = [H[idx:idx+splitSize] for idx in range(0, len(H), splitSize)]
  print(H)
  print(splitString)
  return bytes.fromhex(H)


# MAIN
def main():
  print('### CHALLENGE 00 ###')
  strS_00 = 'My name is Devin Madrigal!'
  print(f'The string to be used is: {strS_00}')
  print(f'The length in bytes of the string is: {chall00(strS_00)}')
  print('\n\n')

  print('### CHALLENGE 01 ###')
  strU_01 = 'https://pythonidae.herokuapp.com/'
  listE_01 = ['web/generate', 'web/identify', 'web/cookies', 'devin/madrigal']
  print(f'The list that will be appended is: {listE_01}')
  print(f'The string that will be appended to each item is: {strU_01}')
  print(f'The new list is: {chall01(strU_01, listE_01)}')
  print('\n\n')

  print('### CHALLENGE 02 ###')
  strD_02 = 'MII CyberSec Consulting Service'
  intS_02 = 0
  intE_02 = 20
  print(f'The string that will be altered is: {strD_02}')
  print(f'The two indexes that will be replaced is: {intS_02} & {intE_02}')
  print(f'The new string is: {chall02(strD_02, intS_02, intE_02)}')
  print('\n\n')

  # print('### CHALLENGE 03 ###')
  # intN_03 = 10
  # intS_03 = 5
  # intE_03 = 8
  # print(chall03(intN_03, intS_03, intE_03))
  # print('\n\n')

  print('### CHALLENGE 04 ###')
  strS_04 = '''
  devinhttps://devin.com hTtP://charles.org
  httP://devin.io
  HTTP://wow2.org
  '''
  print(chall04(strS_04))
  print('\n\n')

  # print('### CHALLENGE 05 ###')
  # strH_05 = '526576657273696e672e4944'
  # print(chall05(strH_05))
  # print('\n\n')


if __name__ == "__main__":
    main()