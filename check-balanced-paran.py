def checkBalancedParans(input_parans):

  stack = []
  openParans = list("{([")
  for i in input_parans:

    if i in openParans:
      stack.append(i)

    else:
      if not stack:
        return False
      popped_paren = stack.pop()
      if i == ")" and popped_paren != "(":
          return False
      elif i == "]" and popped_paren != "[":
          return False
      elif i == "}" and popped_paren != "{":
          return False
  if stack:
    return False
  return True

print(checkBalancedParans("()"))
print(checkBalancedParans("()[]{}"))
print(checkBalancedParans("([)]"))
print(checkBalancedParans("{[]}"))
print(checkBalancedParans(")("))
print(checkBalancedParans("))"))

'''
Balanced paren check is for two checks:
    1. there must always be an opening paren first before subsequent close appears
    2. Then number of open paren should be equal to the closed ones
'''
