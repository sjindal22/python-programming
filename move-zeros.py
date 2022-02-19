def moveZeros(l1):

  zero = 0
  for num in range(0, len(l1)):
    if l1[num] != 0:
      l1[num], l1[zero] = l1[zero], l1[num]
      zero += 1
  return l1    

print(moveZeros([12,0,1,0,3]))
print(moveZeros([4,2,4,0,0,3,0,5,1,0]))

'''
We are using a variable called "zero" to track the position of 0 & since we've
the for loop that will only "do something" when a non "0" value is found, the
idea is to utilize the slow moving value of "zero" to be used as an index for
moving non-zero values. On the other hand use fast moving index of the for loop
to be used for moving 0s to the very end.
'''
