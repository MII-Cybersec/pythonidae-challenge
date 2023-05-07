# Given a dictionary `D`, pair of string `K` and `V`. 
# Add value `V` only if the specified key `K` is not exists. No value replaced.
def chall00(D:dict, K:str, V:str) -> dict:
    if not K in D:
      D[K] = V
    return D

# Given a dictionary `D`. Create a list of all the keys without the values.
def chall01(D:dict) -> list:
    keyList = []
    for key in D.keys():
       keyList.append(key)
    return keyList


# Given a dictionary `D`. Create a list of all the values without the keys.
def chall02(D:dict) -> list:
    valList = []
    for key in D.keys():
       valList.append(D[key])
    return valList


# Given a number `N`. Generate a dictionary where the key is a number from `1` to `N` and the value will be square of the key.
def chall03(N:int) -> dict:
   myDict = {}
   for val in range(1, N+1):
      myDict[val] = val*val
   return myDict


# Given a string `S`. Create a dictionary where the key is a character and the value is the number of its appearance in the string.
# Only existing character appear in the dictionary.
def chall04(S:str) -> dict:
   myDict = {}
   for char in S:
      if char in myDict.keys():
         myDict[char] = myDict.get(char) + 1
      else:
         myDict[char] = 1
   return myDict


# Given a dictionary `D` and a string `K`. Delete key `K` if exist.
def chall05(D:dict, K:str) -> dict:
   if K in D.keys():
      D.pop(K)
   return D


# Given a dictionary `D` and value `V`. Delete every key which have value `V`.
# Note: as alternative, create new dictionary which had eliminated the keys.
def chall06(D:dict, V):
   nonPoppedDict = {}
   poppedDict = {}
   for key in D.keys():
      if D.get(key) == V:
         poppedDict[key] = D.get(key)
      else:
         nonPoppedDict[key] = D.get(key)
   print(f'Dictionary passed in: `{D}`')
   print(f'Old dictionary without popped values: `{nonPoppedDict}`')
   print(f'New dictionary with only popped values: `{poppedDict}`')


# Given two lists `K` and `V`. Create a dictionary where the key-value pair is combination of `K` and `V` at same index.
# Note: handle the case when the length of two lists are not equal.
def chall07(K:list, V:list) -> dict:
   newDict = {}
   for idx, value in enumerate(K if len(K) < len(V) else V):
      newDict[K[idx]] = V[idx]
   return newDict

# Given a list of dictionary `L` and key `K`. Sort the list by the value of key `K`.
def chall08(L:list, K):
  return sorted(L, key=lambda x: x[K])


# Given a list of dictionary `L`.  Remove a common key from each items.
# There is no guarantee that the key exists on each item (dictionary).
# Note: handle exclusion, where certain key is important and must not be removed.
def chall09(L:list, importantKey) -> list:
  commonKeys = set.intersection(*[set(dict.keys()) for dict in L])
  commonKeys.remove(importantKey)
  newList = list(map(
     lambda dict: {key: val for key, val in dict.items() if not key in commonKeys}, L))
  return(newList)


# Given two lists `N` and `C`. Create a new list of dictionaries. 
# The dictionary has two entries, `name` and `code`. The `name` is
#  assigned by element of `N` and `code` is assigned by element of `C`.
def chall10(N:list, C:list) -> list:
  return(list({'name': N[idx], 'code': C[idx]} for idx in range(len(N))))


def main():
  print('### CHALLENGE 00 ###')
  D = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
  existingKeyStr = 'key2'
  existingValStr = 'will not be added!'
  nonExistingKeyStr = 'key4'
  nonExistingValStr = 'will be added!'
  print(f'Let\'s try to add a key/value pair for a key that already exists')
  print(f'Curent Dictionary: {D}')
  chall00(D, existingKeyStr, existingValStr)
  print(f'Now time to check if the new key/value pair was added: {D}')
  print('Now let\'s check for a key/value pair that does not exist in the current dictionary')
  chall00(D, nonExistingKeyStr, nonExistingValStr)
  print(f'New dictionary: {D}')
  print('\n\n')

  print('### CHALLENGE 01 ###')
  D_01 = {"name": "xathrya", "hp": "100", "mp": "32"}
  print(f'Given a dictionary: `{D_01}` return a list of keys')
  print(f'Returned list: {chall01(D_01)}')
  print('\n\n')

  print('### CHALLENGE 02 ###')
  D_02 = {"name": "xathrya", "hp": "100", "mp": "32"}
  print(f'Given a dictionary: `{D_02}` return a list of keys')
  print(f'Returned list: {chall02(D_02)}')
  print('\n\n')

  print('### CHALLENGE 03 ###')
  N_03 = 5
  print(f'Entered value is {N_03}')
  print(f'Returned dictionary {chall03(N_03)}')
  print('\n\n')

  print('### CHALLENGE 04 ###')
  S_04 = 'MII Cybersec'
  print(f'Returned dict: {chall04(S_04)}')
  print('\n\n')

  print('### CHALLENGE 05 ###')
  D_05 = {"key1": 0,"key2": 2,"key3": 5,}
  K_05 = 'key2'
  print(f'Dictionary before removing key: `{K_05}`, Dict: `{D_05}`')
  print(f'New dictionary: {chall05(D_05, K_05)}')
  print('\n\n')

  print('### CHALLENGE 06 ###')
  D_06 = {"key1": 0,"key2": 2,"key3": 5,"key4": 5,}
  V_06 = 5
  chall06(D_06, V_06)
  print('\n\n')

  print('### CHALLENGE 07 ###')
  K_07 = [ "name", "hp", "mp", "love", 'hello', 'world' ]
  V_07 = [ "xathrya", "100", "32", "1000", "devin", 'charles' ]
  print(f'New dictionary: {chall07(K_07, V_07)}')
  print('\n\n')

  print('### CHALLENGE 08 ###')
  L_08 = [ {'key':1}, {'key':10}, {'key':5} ]
  K_08 = 'key'
  L_08 = [ {'key':1}, {'key':10}, {'key':5} ]
  K_08 = 'key'
  sortedList = chall08(L_08, K_08)
  print(f'Original List: {L_08}')
  print(f'Sorted List: {sortedList}')
  print('\n\n')

  print('### CHALLENGE 09 ###')
  L_09 = [ 
     {'id':'1', 'room': '404', 'duration': '4', 'name': 'Jerry'}, 
     {'id':'2', 'room':'405', 'name': 'John'} ]
  importantKey = 'room'
  print(f'Original List of dicts: {L_09}')
  print(f'New List of dicts: {chall09(L_09, importantKey)}')
  print('\n\n')

  print('### CHALLENGE 10 ###')
  N_10 = [ "black", "red", "maroon", "yellow", "white'"]
  C_10 = [ "#000000", "#FF0000", "#800000", "#FFFF00", "#FFFFFF"]
  print(chall10(N_10, C_10))
  
if __name__ == "__main__":
    main()