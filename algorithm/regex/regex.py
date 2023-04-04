import re  #Built-in RegEx Python package


# Given a possible long text, find and extract valid IPv4 addresses.
# An IPv4 address consists of 4 segments, separated by a dots. 
# Each segment is a value ranged from 0 to 255.
def chall00(longText:str) -> list:
   ipv4Regex = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
   return re.findall(ipv4Regex, longText)
   

# Given a possible long text, find and extract valid IPv6 addresses.
# An IPv6 address consists of 8 segments, separated by colons. 
# Each segment is four hexadecimal digits which value ranged from 0 to ffff.
def chall01(longText:str) -> list:
   ipv6Regex = r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
   return re.findall(ipv6Regex, longText)


# MAIN
def main():
  print('### CHALLENGE 00 ###')
  # Example IPv4 address: 123.89.66.72
  longText_00 = 'devin123.89.66.72dfas f192.168.0.1 10.-4.244.1, 123.123.123.123'
  print(chall00(longText_00))
  print('\n\n')

  # print('### CHALLENGE 01 ###')
  # longText_01 = '''
  # 128d:84cd:c839:f90b:fbcd:c628:2b75:e48e 
  # 128d:84cd::c628:2b75:e48e 
  # notAvalidIPv6Address 
  # Hello my name is Devin :) 
  # 128d:84cd:0000:0000:0000:c628:2b75:e48e
  # df69:1ed6:2bf0:a02c:bcad::12dd:3744 
  # 2001:0db8::8a2e:370:7334 
  # 2001:0db8:0000:0000:0000:8a2e:0370:7334
  # '''
  # print(chall01(longText_01))
  # print('\n\n')

  # print('### CHALLENGE 02 ###')
  # print('\n\n')

  # print('### CHALLENGE 03 ###')
  # print('\n\n')

  # print('### CHALLENGE 04 ###')
  # print('\n\n')

  # print('### CHALLENGE 05 ###')
  # print('\n\n')

  # print('### CHALLENGE 06 ###')
  # print('\n\n')

  # print('### CHALLENGE 07 ###')
  # print('\n\n')
  
if __name__ == "__main__":
    main()