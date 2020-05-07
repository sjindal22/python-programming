l1 = [1,2,3,[4,5],[6,[7,8,9],10], 11]
l2 = []

def flattenList(l1):

  for i in l1:
    if type(i) == list:
      flattenList(i)
    else:
      l2.append(i)
  return l2

print(flattenList(l1))

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""
