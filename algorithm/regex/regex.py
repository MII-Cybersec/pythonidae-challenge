import re  #Built-in RegEx Python package
import ipaddress


# Given a possible long text, find and extract valid IPv4 addresses.
# An IPv4 address consists of 4 segments, separated by a dots. 
# Each segment is a value ranged from 0 to 255.
def chall00(longText:str) -> list:
   pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
   return re.findall(pattern, longText)
   

# Given a possible long text, find and extract valid IPv6 addresses.
# An IPv6 address consists of 8 segments, separated by colons. 
# Each segment is four hexadecimal digits which value ranged from 0 to ffff.
def chall01(longText: str) -> list:
    pattern = r'((?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'

    # Find all matches of the IPv6 pattern in the input string
    # ipv6_addresses = re.findall(ipv6_pattern, longText)
    # match = re.findall(pattern, longText)
    # return match
    return [result[0] for result in re.findall(pattern, longText)]


# Given a possible long text, find and extract domain names. Domain name consists of several string, 
# separated by dots. The right most string is top-level domain, which value is defined (i.e. com, net, id, org).
# The rest are defining hostnames, which can be any arbitrary string.
def chall02(longText):
    pattern = r'^(?:\s*)(?:\w+.)+(?:com|net|id|org)(?:\s*)$'
    matches = re.finditer(pattern,longText, re.MULTILINE)
    return [match.group() for match in matches]


# Given a possible long text, find and extract valid email addresses.
#  An email address consists of two parts username and domain, which separated by @.
def chall03(S:str):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.finditer(pattern, S)
    return [match.group() for match in matches]


def chall04(S:str):
    pattern = r'\b\d{3}[- ]?\d{2}[- ]?\d{4}\b|\b\d{9}\b'
    matches = re.findall(pattern, S)
    return matches


# Given a long text `S`. Find and extract only 3-digit numbers. If 3 digits are part of larger number 
# (4 or more digits) then this number is excluded. The 3-digit numbers must be preceeded by and followed by a non-word character.
def chall05(S:str):
    pattern = r'\b(\d{3})\b'
    matches = re.findall(pattern, S)
    return matches


# Given a possible long text, find and extract HTML tags and list its attibutes.
def chall06(text:str) -> dict:
  pattern = r'<\w+(?:\s(?:\w+="[\w\s/.]*"))*>'
  matches = re.finditer(pattern, text, re.MULTILINE)
  matchesList = [match.group() for match in matches]
  tagsDict = []
  for match in matchesList:
    split = match.strip('<>').split(' ')  
    tagsDict.append(split[0])
    tagsDict.append(split[1:])
  return tagsDict


def chall07(text:str):
    pattern = r'^[^:]+:\$([^\$]+)\$([^\$]+)\$([^\$]+)'

    # Use the regular expression to extract the three fields
    match = re.match(pattern, text)
    if match:
        cipherAlg = match.group(1)
        salt = match.group(2)
        passHash = match.group(3)
        return (cipherAlg, salt, passHash)
    else:
        return None


# MAIN
def main():
  print('### CHALLENGE 00 ###')
  # Example IPv4 address: 123.89.66.72
  longText_00 = 'devin123.89.66.72dfas f192.168.0.1 10.-4.244.1, 123.123.123.123'
  print(chall00(longText_00))
  print('\n\n')

  print('### CHALLENGE 01 ###')
  longText_01 = '''
    1762:0:0:0:0:B03:1:AF18
    128d:84cd:c839:f90b:fbcd:c628:2b75:e48e
    128d:84cd::c628:2b75:e48e
    notAvalidIPv6Address
    Hello my name is Devin :)
    128d:84cd:0000:0000:0000:c628:2b75:e48e
    df69:1ed6:2bf0:a02c:bcad::12dd:3744
    2001:0db8::8a2e:370:7334
    54ej:6fnd:3200:5478:30de:edeb:3189
    2001:0db8:0000:0000:0000:8a2e:0370:7334
    '''
  print(chall01(longText_01))
  print('\n\n')

  print('### CHALLENGE 02 ###')
  longText_02 = ("google.com\n"
	"devin..org\n"
	"google.net\n"
	"id.org.devin\n"
	"devin.is.awesome.org\n"
	"charles.and.bella.id")
  print(chall02(longText_02))
  print('\n\n')

  print('### CHALLENGE 03 ###')
  S_03 = ('devinmadr@gmail.com\n' 
          'helloworld@yahoo.com\n' 
          'CharlesXavier@yahoo.net\n' 
          'invalidUsername\n' 
          '@invalidComain.net')
  print(chall03(S_03))
  print('\n\n')

  print('### CHALLENGE 04 ###')
  S_04 = 'This is a test string with 123-45-6789, 123 45 6789, 123456789 social security numbers and an invalid number 12345678.'
  print(chall04(S_04))
  print('\n\n')

  print('### CHALLENGE 05 ###')
  # S_05 = 'This is a test string with 123 and 4567 and 890 and 013 and some punctuation marks, like ! and ?.'
  S_05 = '123 5678 013'
  print(chall05(S_05))
  print('\n\n')

  print('### CHALLENGE 06 ###')
  text_06 = ('<img src="image.jpg" alt="A beautiful sunset">\n' 
    '<h1>Submission Form</h1>\n'
    '<form action="/submit" method="post">\n' 
    '<input type="text" name="username" placeholder="Username">\n'
    '<input type="password" name="password" placeholder="Password">\n'
    '<input type="submit" value="Submit"> \n'
    '</form>')
  print(chall06(text_06))
  print('\n\n')

  print('### CHALLENGE 07 ###')
  # text_07 = 'user1' + ':' + '$' + '6' + '$' + 'Abcd1234' + '$' + '5iH4G7Jk8lM9n0P1qR2s3t4u5v6w7x8y9zA.BCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdef/:18475:0:99999:7:::'
  text_07 = 'sai' + ':' + '$' + '6' + '$' + 'YTJ7JKnfsB4esnbS' + '$' + '5XvmYk2.GXVWhDo2TYGN2hCitD/wU9Kov.uZD8xsnleuf1r0ARX3qodIKiDsdoQA444b8IMPMOnUWDmVJVkeg1:19446:0:99999:7:::'
  # text_07 = 'raj' + ':' + '$' + 'y' + '$' + 'j9T' + '$' + '5KGIS/2Ug.47GjW0jHOIB/XwYUafYPh/petN8gKSJuLt5CEbBya3dW3pIgwrS3eJB:19447:0:99999:7:::'
  print(chall07(text_07))
  print('\n\n')
  
if __name__ == "__main__":
    main()