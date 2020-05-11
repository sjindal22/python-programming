def jumpGame(l1):

  steps = 0
  for i, v in enumerate(l1):
    if i > steps:
      return False
    steps = max(steps, i+v)
  return True

print(jumpGame([2,3,1,1,4]))
print(jumpGame([3,2,1,0,4]))
