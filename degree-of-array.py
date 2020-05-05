def minSubtring(arr):

  first, count, response, degree = {}, {}, 0, 0

  for i, a in enumerate(arr):
    
    first.setdefault(a,i)
    count[a] = count.get(a,0) + 1
   
    if count[a] > degree:
      degree = count[a]
      response = i - first[a] + 1

    elif count[a] == degree:
      response = min(response, i - first[a] + 1)

  return response

print(minSubtring([1,2,2,3,1,1]))
print(minSubtring([1,2,2,3,1]))

"""
Output:
6
2
"""
