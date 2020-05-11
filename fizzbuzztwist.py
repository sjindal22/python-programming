def fizzbuzztwist(inputNum):

  finalList = []
  d = {3: "Fizz", 5: "Buzz", 7: "Jazz"}

  for n in range(1, inputNum+1):

    str_num = ""
    for i in d.keys():

      if n%i  == 0:
        str_num += d[i]
    
    if not str_num:
      str_num = str(n)    

    finalList.append(str_num)

  return finalList

print(fizzbuzztwist(40))

"""
O/P:
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Jazz', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', 'Jazz', 'FizzBuzz', '16', 
'17', 'Fizz', '19', 'Buzz', 'FizzJazz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', 'Jazz', '29', 'FizzBuzz', '31', 
'32', 'Fizz', '34', 'BuzzJazz', 'Fizz', '37', '38', 'Fizz', 'Buzz']
"""
