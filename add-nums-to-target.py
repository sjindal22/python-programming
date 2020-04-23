def addNums(l1, target):

  d = {}
  if len(l1) <= 1:
    return False
  for i, n in enumerate(l1):
    m = target - n
    if m in d:
      return [d[m], i]
    else:
      d[n] = i

print(addNums([2,7,11,15], 9))
print(addNums([2,7,11,15], 26))
print(addNums([2], 2))
