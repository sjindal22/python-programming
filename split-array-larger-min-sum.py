def splitArray(arr):

  sum = 0
  index = 0
  current_sum = 0
  n = len(arr)
 
  for i in range(n):
    sum += arr[i]
  
  split = int(sum/2)

  arr.sort(reverse=True)

  for i in range(n):
    current_sum += arr[i]
    index += 1

    if current_sum > split:
      return sorted(arr[:index])

  return sorted(arr[:index])

print(splitArray([3, 1, 7, 1]))
print(splitArray([3,7,5,6,2]))
print(splitArray([2,3,4,4,5,9,7,8,6,10,4,5,10,10,8,4,6,4,10,1]))
