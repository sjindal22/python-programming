from collections import defaultdict

def findIndices(l1, target):

  if target not in l1:
    return [-1, -1]

  first = l1[0]
  if l1 == [first]*len(l1):
    return [0, len(l1)-1]
  

  else:
    d = defaultdict(list)
    for i,x in enumerate(l1):
      d[str(x)].append(i)


    for i,v in d.items():
      if i == str(target):
        v = [v[0], v[-1]]
        return v

print(findIndices([5,7,7,8,8,10], 8)) 
print(findIndices([5,7,7,8,8,10], 6)) 
print(findIndices([1], 1)) 
print(findIndices([1,4], 4)) 
print(findIndices([3,3,3], 3)) 
