def minSquares(x): 
  
    # base cases 
    if x <= 3: 
        return x; 
  
    # minSquares rest of the table  
    # using recursive formula 
    result = x 
  
    # Go through all smaller numbers 
    # to recursively find minimum 
    for y in range(1, x + 1): 
        temp = y * y 
        if temp > x: 
            break
        else: 
            result = min(result, 1 + minSquares(x  
                                  - temp)) 
      
    return result

print(minSquares(6))

"""
op: 3
2^2, 1^1, 1^1
"""
