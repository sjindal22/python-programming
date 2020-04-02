# Find the largest number in a list

# Method 1

l1 = [1,1,4,2,3]
l1.sort()
print(l1[-1])

# Method 2

l1 = [1,1,4,2,3]
l1 = max(l1)
print(l1)

# Method 3

def largest_number(arr):

  max = arr[0]
  
  for i in range(1, len(arr)):
    if arr[i] > max:
      max = arr[i]
  return max

print(largest_number([10, 324, 45, 90, 9808]))
