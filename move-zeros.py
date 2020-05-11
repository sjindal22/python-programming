def moveZeros(l1):

  zero = 0
  for num in range(0, len(l1)):
    if l1[num] != 0:
      l1[num], l1[zero] = l1[zero], l1[num]
      zero += 1
  return l1    

print(moveZeros([12,0,1,0,3]))
print(moveZeros([4,2,4,0,0,3,0,5,1,0]))
