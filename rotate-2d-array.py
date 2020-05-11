def rotate(arr):

  arr[:] = map(list, zip(*arr[::-1]))
  return arr

x = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(rotate(x))
