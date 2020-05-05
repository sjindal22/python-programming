def rotate(arr, k):

  n = len(arr)
  k = k%n
  arr[:] = arr[n-k:] + arr[:n-k]

  return arr

print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))

"""
[5, 6, 7, 1, 2, 3, 4]
[3, 99, -1, -100]
"""
