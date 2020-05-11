def findSingleNum(inputList):

  d = {}
  for num in inputList:
    d[num] = d.get(num, 0) + 1

  for k in d:
    if d[k] == 1:
      return k


print(findSingleNum([4,1,2,1,2]))
print(findSingleNum([2,2,1]))
  
