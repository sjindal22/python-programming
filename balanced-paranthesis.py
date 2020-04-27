# Python3 program to 
# Print all combinations 
# of balanced parentheses 
  
# Wrapper over _printParenthesis() 
def printParenthesis(str, n): 
    if(n > 0):
        _printParenthesis(str, 0,  
                          n, 0, 0) 
    return
  
def _printParenthesis(str, pos, n,  
                      open, close): 
      
    if(close == n): 
        for i in str: 
            print(i, end = "")
        print() 
        return 
    else: 
        if(open > close): 
            str[pos] = '}'; 
            _printParenthesis(str, pos + 1, n,  
                              open, close + 1) 
        if(open < n): 
            str[pos] = '{'; 
            _printParenthesis(str, pos + 1, n,  
                              open + 1, close) 
  
# Driver Code 
n = 3; 
str = [""] * 2 * n; 
printParenthesis(str, n);

"""
def generateParenthesis(n):
    def generate(p, left, right, parens=[]):
        if left: 
            print("Left call")        
            generate(p + '(', left-1, right)
        if right > left:
            print("Right call")        
            generate(p + ')', left, right-1)
        if not right:
            print("Not Right call")        
            parens += p
        print("Printing....", parens),
        return parens
    return generate('', n, n)

print(generateParenthesis(3))
"""
