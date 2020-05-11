from collections import OrderedDict
def findMissingNum(l1):

  d = OrderedDict()
  for i in range(0, len(l1)+1):
    d[str(i)] = i

  l1 = sorted(l1)
  for x, y in zip(l1, d.values()):
    if x-y != 0:
      return y
    elif x == l1[-1]:
      return x + 1 

print(findMissingNum([9,6,4,2,3,5,7,0,1]))
print(findMissingNum([0]))

  
