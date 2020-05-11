"""
1. Assign some temporary variables, where result = emptry string, count = 1 and tmp = first character of the string.
2. Enumerate through each item in the string.
   a. If character == tmp, increment the counter by 1.
   b. Else:
      i. if count == 1, result is just the tmp variable.
      2. else, result = string combination of charcter in the string, with last index value  + its count.
      3. Reset the count and tmp
3. Finally, catch for the last iteration:
   a. if count == 1, result is just the tmp variable.
   b. else, result = string combination of the current item  + its count.
"""


def countNum(s):

  count = 1
  tmp = s[0]
  result = ""

  for i, item in enumerate(s[1:]):
    if item == tmp:
      count += 1
      
    else:
      if count == 1:
        result += tmp
      else:
        result += (s[i-1]+ str(count))
      count = 1
      tmp = item

  if count == 1:
    result += item
  else:
    result += (item + str(count))

  return result

print(countNum("aaabbb"))
print(countNum("aaccaabbb"))
print(countNum("aacaabbb"))
