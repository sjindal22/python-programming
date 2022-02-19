def doIt(num):

  # Reverse Integer

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

print(doIt(123))
print(doIt(-123))
print(doIt(120))
print(doIt(1534236469))
