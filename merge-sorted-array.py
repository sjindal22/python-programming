def mergeSortedArray(l1, m, l2, n):

  while m > 0 and n > 0:
    if l1[m - 1] >= l2[n - 1]:
      l1[m+n-1] = l1[m-1]
      m -= 1

    else:
      l1[m+n-1] = l2[n-1]
      n -= 1

  return l1

print(mergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3))

"""
op:
[1,2,2,3,5,6]
"""
