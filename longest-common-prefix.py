"""
1. Find the word in the list with minimum number of characters.
   a. min(iterator, key= len) -> will achieve that.
2. Iterate through each character in the shortest word.
   a. Start an inner loop with the original list.
   b. If index of the word in the bigger list, does not match the character in the shortest word,
      return the characters in the shortest word, until that index.
"""


def commonPrefix(l1):

  shortest = min(l1, key=len)
  for i, char in enumerate(shortest):

   for word in l1:
     if word[i] != char:
       return shortest[:i]

print(commonPrefix(["flower","flow","flight"]))
print(commonPrefix(["dog","racecar","car"]))
