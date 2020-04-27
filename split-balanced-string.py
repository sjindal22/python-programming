from itertools import accumulate

def numBalancedStrings(inputString):

  return list(accumulate(1 if c == 'L' else -1 for c in inputString)).count(0)

print(numBalancedStrings("RLRRLLRLRL"))
print(numBalancedStrings("RLLLLRRRLR"))
