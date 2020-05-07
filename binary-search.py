"""
Binary Search: Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. If the value of the search key is less 
than the item in the middle of the interval, narrow the interval to the lower half. 
Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
"""

def binarySearch(n, arr, length, r):
 
  if r >= length:
    mid = length + (r - length) // 2

    if arr[mid] == n:
      return mid

    elif n > arr[mid]:
      return binarySearch(n, arr, mid+1, r)

    else:
      return binarySearch(n, arr, length, mid-1)

  else:
    return -1


arr = [2, 3, 4, 10, 40]
n = 3
result = binarySearch(n, arr, 0, len(arr)-1)
print(result)
