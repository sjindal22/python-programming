def commonPrefix(l1: list) -> str:

  shortest = min(l1, key=len)
  for i, char in enumerate(shortest):

   for word in l1:
     if word[i] != char:
       return f'"{shortest[:i]}"'

print(commonPrefix(["flower","flow","flight"]))
print(commonPrefix(["dog","racecar","car"]))

"""
O/P:
"fl"
""
1. min function returns the minimum value. If the value is a string the minium 
would be the one arranged alphabetically. Remember min for string does not mean
shortest string with minimum number of characters.

2. shortest = min(l1, key=len). Here key is the conditional check to be done on
the minimum/shortest string returned. Therefore, even if "flight" is the minimum,
the len of it is greater than "flow". Therefore, "flow" is the shortest.
"""
