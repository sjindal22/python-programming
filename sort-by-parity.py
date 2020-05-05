def sortByParity(lst):

  print("Input is {}".format(lst))
  opLst = [None]*len(lst)
  start = 0
  end = len(lst) - 1
  for var in lst:
    if var % 2 == 1:
      opLst[end] = var
      end -=1
    else:
      opLst[start] = var
      start +=1

  return opLst

print(sortByParity([3,1,2,4]))
