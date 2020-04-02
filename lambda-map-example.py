# Map - works on func, iterable

def addition(n):
  return n + n

print(list(map(addition, (1,2,3,4))))

# Lambda also takes func, itertable but takes a library func/ad-hoc one

l1 = [1,2,3,4]
l2 = [5,6,7,8]

y = list((map(lambda x, y: x + y, l1, l2)))
print(y)


# Gotcha

# To split a string into list
# You can use list function, which can create a list of elements without using explicit "for" loop
# You cannot create a list of another list using the following methodology as the result remains the same

name = "Shivika"
print(list(name))
print(sorted(name))
