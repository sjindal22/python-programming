def fillContainer(l1):

  unique_coordinates = list(set(l1))
  largest = unique_coordinates[-1]

  if len(unique_coordinates) >= 2:
    second_largest = unique_coordinates[-2]
  else:
    second_largest = largest

  for i, v in enumerate(l1[::-1]):
  
    if v == largest or v == second_largest:
      l = v
      b = l1.index(v)
      if b == 0:
        b += 1
      break
  
  for x,y in enumerate(l1):

    if l == second_largest:
      if y == second_largest or y < second_largest:
         b = b - x
         break
    else:
      if y == largest or y == second_largest:
         b = b - x
         break

  return l*b

print(fillContainer([1,8,6,2,5,4,8,3,7]))
print(fillContainer([1,2]))
print(fillContainer([1,1]))
