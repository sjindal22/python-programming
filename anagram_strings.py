# Method 1

def checkIfAnagrams(str1, str2):

  if len(str1) != len(str2):
    return False

  if sorted(str1) == sorted(str2):
    return True

  else:
    return False

print(checkIfAnagrams("acdb", "abdc"))
print(checkIfAnagrams("acdb", "abdcd"))
print(checkIfAnagrams("aadb", "abdc"))
print(checkIfAnagrams("aadb", "daba"))

"""
O/P:
True
False
False
True
"""

# Method 2
def checkIfAnagrams(str1, str2):

  if len(str1) != len(str2):
    return False

  else:
    def compare(input_string):
      d = {}
      for i in input_string:
        if i in d.keys():
          d[i] += 1
        else:
          d[i] = 1
      return d

  return compare(str1) == compare(str2)

print(checkIfAnagrams("acdb", "abdc"))
print(checkIfAnagrams("acdb", "abdcd"))
print(checkIfAnagrams("aadb", "abdc"))
print(checkIfAnagrams("aadb", "daba"))

"""
O/P:
True
False
False
True
"""
