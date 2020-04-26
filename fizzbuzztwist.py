def fizzbuzztwist(inputNum):

  finalList = []
  d = {3: "Fizz", 5: "Buzz", 7: "Jazz"}

  for n in range(1, inputNum+1):

    str_num = ""
    for i in d.keys():

      if n%i  == 0:
        str_num += d[i]
        finalList.append(str_num)
    
    if not str_num:
      finalList.append(str(n))    

  return finalList

print(fizzbuzztwist(40))
