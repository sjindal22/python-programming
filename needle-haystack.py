"""
1. Start a for loop for the range (len(needle) - len(hay) + 1)
2. Compare if needle[i:len(needle)+i] == hay
"""


def findNeedle(haystack, needle):

  for i in range(len(haystack) - len(needle) + 1):

    if(haystack[i:i+len(needle)] == needle):
      return i

  return -1

print(findNeedle("hello", "ll"))
print(findNeedle("aaaaa","bba"))

"""
OP:
2
-1
"""
