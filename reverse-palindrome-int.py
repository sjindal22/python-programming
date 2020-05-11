"""
1. Split cases between negatives and positives.
2. If num is a single digit number, return num itself.
3. Else check if last digit in the number is 0 or not, 
   a. If it is, truncate it.
4. Else, just reverse the num and check if it in the range of -2^31 and 2^31-1

"""

def reverseSingedInteger(num):

  if num > 2147483647 or num < (-2147483648):
    return 0

  if num < 0:
    if -1 <= num <= -9:
      num = abs(num)
      return int("-" + str(num))
    elif str(num)[-1] == 0:
      num = abs(num)
      return int("-" + str(num[:-1])[::-1])
    else:
      num = abs(num)
      num = int("-" + str(num)[::-1])
      if num < (-2147483648):
        return 0
      else:
        return num


  else:
    if 0 <= num <= 9:
      return num
    elif str(num)[-1] == 0:
      return int(str(num[:-1])[::-1])
    else:
      num = int(str(num)[::-1])
      if num > 2147483647:
        return 0
      else:
        return num

print(reverseSingedInteger(123))
print(reverseSingedInteger(-123))
print(reverseSingedInteger(120))
print(reverseSingedInteger(1534236469))
