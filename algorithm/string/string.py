from random import randbytes, randint
from binascii import unhexlify
from itertools import permutations


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
      bList.append(randint(0,255))
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
  print(f'Entered String and size: {H}, {len(H)}')
  splitSize = 2
  splitStringList = [H[idx:idx+splitSize].encode('utf-8') for idx in range(0, len(H), splitSize)]
  print(f'Returned sequence of bytes and size: {splitStringList}, {len(splitStringList)}')


# Given a string `S` and single-byte `C`. XOR each character of `S` with `C`. 
# The result bytes might not be printable characters. Hint: Operate in `bytes` object is recommended.
def chall06(S:str, C:bytes):
  splitSize = 2
  splitHexString =[S[idx:idx+splitSize] for idx in range(0, len(S), splitSize)]
  
  newXorStr = ''
  for idx in splitHexString: newXorStr = f"{newXorStr}{convertToHexStr06(getXor(convertToBinaryStr(idx), convertToBinaryStr(C.decode('utf-8'))))}"
  return newXorStr

def convertToHexStr06(binaryStr:str) -> str:
  return "{0:0>2X}".format(int(binaryStr, base=2))


# Given two equal-length hexpair string S1 and S2. XOR S1 and S2.
# Hint: Operate in bytes object is recommended.
def chall07(S1:str, S2:str) -> str:
  binary_S1 = convertToBinaryStr(S1)
  binary_S2 = convertToBinaryStr(S2)
  binaryXorResult = getXor(binary_S1, binary_S2)
  return convertToHexStr(binaryXorResult)

def convertToBinaryStr(hexStr:str) -> str:
  return "{0:08b}".format(int(hexStr, base=16))

def getXor(strBin01:str, strBin02:str):
  y=int(strBin01,2) ^ int(strBin02,2)
  return ('{0:b}'.format(y))

def convertToHexStr(binaryStr:str) -> str:
  return "{0:0>4X}".format(int(binaryStr, base=2))


# Given two unequal-length hexpair string, S1 and S2, with S1 always longer than S2.
# XOR S1 and S2. Also, try to handle when S1 is shorter than S2.
# Hint: Operate in bytes object is recommended.
def chall08(S1:str, S2:str) -> str:
  while len(S2) < len(S1):
    S2 = S2 * 2
  S2 = S2[-(len(S1)):]
  binary_S1 = convertToBinaryStr(S1)
  binary_S2 = convertToBinaryStr(S2)
  binaryXorResult = getXor(binary_S1, binary_S2)
  return convertToHexStr(binaryXorResult)


# Given a string with length N. Generate all possible permutation of the string.
def chall09(N:str) -> list:
  return [''.join(x) for x in permutations(N)]


# Given a string S and list of integer P, both have the same length N. 
# Each element of list P is a unique number which value is in range 0 to N-1.
# Create a new string T, which is permutation of S using P as index.
def chall10(S:str, P:list) -> str:
  newStr:str = ''
  for idx in P:
    newStr += S[idx]
  return newStr


# MAIN
def main():
  # print('### CHALLENGE 00 ###')
  # strS_00 = 'My name is Devin Madrigal!'
  # print(f'The string to be used is: {strS_00}')
  # print(f'The length in bytes of the string is: {chall00(strS_00)}')
  # print('\n\n')

  # print('### CHALLENGE 01 ###')
  # strU_01 = 'https://pythonidae.herokuapp.com/'
  # listE_01 = ['web/generate', 'web/identify', 'web/cookies', 'devin/madrigal']
  # print(f'The list that will be appended is: {listE_01}')
  # print(f'The string that will be appended to each item is: {strU_01}')
  # print(f'The new list is: {chall01(strU_01, listE_01)}')
  # print('\n\n')

  # print('### CHALLENGE 02 ###')
  # strD_02 = 'MII CyberSec Consulting Service'
  # intS_02 = 0
  # intE_02 = 20
  # print(f'The string that will be altered is: {strD_02}')
  # print(f'The two indexes that will be replaced is: {intS_02} & {intE_02}')
  # print(f'The new string is: {chall02(strD_02, intS_02, intE_02)}')
  # print('\n\n')

  print('### CHALLENGE 03 ###')
  intN_03 = 10
  intS_03 = 5
  intE_03 = 8
  print(chall03(intN_03, intS_03, intE_03))
  print('\n\n')

  # print('### CHALLENGE 04 ###')
  # strS_04 = '''
  # devinhttps://devin.com hTtP://charles.org
  # httP://devin.io
  # HTTP://wow2.org
  # '''
  # print(chall04(strS_04))
  # print('\n\n')

  print('### CHALLENGE 05 ###')
  strH_05 = '526576657273696e672e4944'
  chall05(strH_05)
  print('\n\n')

  print('### CHALLENGE 06 ###')
  strS_06 = '526576657273696e672e4944'
  bytesC_06 = b'53'
  print(f'The hexpair string: {strS_06}')
  print(f'The byte to XOR by: {bytesC_06}')
  print(f'The returned result: {chall06(strS_06, bytesC_06)}')
  print('\n\n')

  print('### CHALLENGE 07 ###')
  strS1_07 = '44355050f07a7e2df0067d45'
  strS2_07 = '165026358209174397283401'
  print(f'Hex String 1: {strS1_07}')
  print(f'Hex String 2: {strS2_07}')
  print(f'Xor result: {chall07(strS1_07, strS2_07)}')
  print('\n\n')

  print('### CHALLENGE 08 ###')
  strS1_08 = 'd5577f20f541602be01c4001'
  strS2_08 = '87320945'
  print(f'Hex String 1: {strS1_08}')
  print(f'Hex String 2: {strS2_08}')
  print(f'Xor result: {chall08(strS1_08, strS2_08)}')
  print('\n\n')

  print('### CHALLENGE 09 ###')
  strN_09 = 'ABC'
  print(f'String: {strN_09}')
  print(f'All permutations: {chall09(strN_09)}')
  print('\n\n')

  print('### CHALLENGE 10 ###')
  strS_10 = 'MII-CyberSec'
  listP_10 = [4, 0, 9, 5, 6, 10, 2, 8, 1, 7, 3, 11]
  print(f'String: {strS_10}')
  print(f'List of ints: {listP_10}')
  print(f'New string: {chall10(strS_10, listP_10)}')
  print('\n\n')

if __name__ == "__main__":
    main()