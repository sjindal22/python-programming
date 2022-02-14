def addNums(l1, target):

#Method 1
  d = {}
  if len(l1) <= 1:
    return False
  for i, n in enumerate(l1):
    m = target - n
    if m in d:
      return [d[m], i]
    else:
      d[n] = i

#Method 2

def addNums(l, t):
    if len(l) == 1 and l[0] == t:
        return 0
    for i, n in enumerate(l):
        temp = t - n
        if temp in l:
            return [i, l.index(temp)]
        else:
            continue
    return "Matching pair not found!" 

print(addNums([2,7,11,15], 9))
print(addNums([2,7,11,15], 26))
print(addNums([2,7,11,15], 27))
print(addNums([-3,4,3,90], 0))
print(addNums([2], 2))
print(addNums([3], 2))

'''
O/P
[0, 1]
[2, 3]
Matching pair not found!
[0, 2]
0
Matching pair not found!
'''
