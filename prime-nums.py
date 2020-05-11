import math
def isPrime(n):

  primes = [2,3,5,7]
  count = 2
  primeCount = 0

  for num in range(2, n):

    if num in primes:
      primeCount += 1

    x = math.sqrt(num)
    y = math.floor(x)
    if (x-y) == 0:
      continue
    
    else:
      for i in primes:
        if num%i == 0:
          count += 1
 
      if count <= 2:
        primeCount += 1    
    
    count = 2    

  return primeCount

print(isPrime(10)) 
print(isPrime(20)) 
print(isPrime(30)) 
print(isPrime(122)) 
print(isPrime(125)) 
