"""
1. Starting from the number 1, compare square of each number with the given number, to see if it is lesser than the given number.
2. Once the condition is unsatisfied, previously squared number was the value.
3. For eg, 1^2 < 8, 2^2 <8, 3^2 != 8. Therefore, 2 is the answer.

"""

def floorSqrt(x):

  result = 0
  i = 1

  while result < x:
   i += 1
   result = i*i

  return i-1

print(floorSqrt(4)) 
print(floorSqrt(8)) 
print(floorSqrt(111)) 
print(floorSqrt(11)) 

"""
OP:
1
2
10
3
"""
