# Method 1

def int_to_list(x):

  y = [int(x) for x in str(x)]
  return y

print(int_to_list(5))
print(int_to_list(2020))

# Method 2 (using map function)

y = list(map(int, str(2020)))
print(y)
