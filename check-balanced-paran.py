def checkBalancedParans(input_parans):

  stack = []
  openParans = list("{([")
  for item in input_parans:

    if item in openParans:
      stack.append(item)

    else:
      if not stack:
        return False
      closeParanChar = stack.pop()
      if closeParanChar == "{":
        if item != "}":
          return False
      if closeParanChar == "(":
        if item != ")":
          return False
      if closeParanChar == "[":
        if item != "]":
          return False
  if stack:
    return False
  return True

print(checkBalancedParans("()"))
print(checkBalancedParans("()[]{}"))
print(checkBalancedParans("([)]"))
print(checkBalancedParans("{[]}"))

'''
Balanced paren check is for two checks:
    1. there must always be an opening paren first before subsequent close appears
    2. Then number of open paren should be equal to the closed ones
'''
