def validParen(s):

  """
  define a stack and dictionary and run a loop for each char
  """
  stack = []
  d = {"]":"[", "}":"{", ")":"("}

  for alphabet in s:
    
    if alphabet in d.values():
      stack.append(alphabet)

    elif alphabet in d.keys():
      if stack == [] or d[alphabet] != stack.pop():
        return False

    else:
      False

  return stack == []

print(validParen("()"))
print(validParen("()[]{}"))
print(validParen("([)]"))

