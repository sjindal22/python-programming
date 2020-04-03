def splitIndex(l1):

  leftSum = 0
  for i in range(0, len(l1)):
    leftSum += l1[i]

  rightSum = 0
  for i in range(len(l1)-1, -1, -1):
    rightSum += l1[i]

    leftSum -= l1[i]

    if(rightSum == leftSum):
      return i
  
  return -1

def splitList(l1):

  index = splitIndex(l1)
  
  if(index == -1):
    print("list cannot be split into two lists with equal sum")
    return
  
  for i in range(0, len(l1)):
    if i == index:
      print("\nAnother list")
    print(l1[i], end = " ")
  print("")

splitList([1,2,3,4,5,5])

"""
O/P:
1 2 3 4 
Another list
5 5 
"""
