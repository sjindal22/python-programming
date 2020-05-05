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
