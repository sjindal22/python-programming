def rotate(arr):

  arr[:] = map(list, zip(*arr[::-1]))
  larry = len(arr)
  for i in range(larry):
      if i == 0:
          print("[",arr[i])
      elif i == larry-1:
          print(arr[i], "]")
      else:
          print(arr[i])

x = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(x)

'''
arr[::-1] -> Creates a shallow reversed copy of the original array

[[7,8,9], [4,5,6], [1,2,3]]

zip(*arr[::-1]) -> unpacking the arguments using zip. Remember during unpacking,
the first element from iterator is taken, then second, so on and so forth.

[[7,4,1], [8,5,2], [9,6,3]]
or
[ [7, 4, 1]
[8, 5, 2]
[9, 6, 3] ]
'''
