import numpy

def returnMatrixSize(screen):

   r, c = (numpy.array(screen)).shape
   return r,c

def fillFloodUtil(screen, x, y, newC, m, n, prevC):

  if(x < 0 or x >= m or y < 0 or y >= m or screen[x][y] == newC or screen[x][y] != prevC):
    return

  screen[x][y] = newC 
  fillFloodUtil(screen, x+1, y, newC, m, n, prevC)
  fillFloodUtil(screen, x-1, y, newC, m, n, prevC)
  fillFloodUtil(screen, x, y+1, newC, m, n, prevC)
  fillFloodUtil(screen, x, y-1, newC, m, n, prevC)

def floodFill(screen, x, y, newC, m,n):

  prevC = screen[x][y]
  fillFloodUtil(screen, x, y, newC, m, n, prevC=prevC)

screen = [[1, 1, 1, 1, 1, 1, 1, 1],  
          [1, 1, 1, 1, 1, 1, 0, 0],  
          [1, 0, 0, 1, 1, 0, 1, 1],  
          [1, 2, 2, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 2, 2, 0],  
          [1, 1, 1, 1, 1, 2, 1, 1],  
          [1, 1, 1, 1, 1, 2, 2, 1]] 
print(screen)
print()

m, n = returnMatrixSize(screen)
x, y = 4,4

floodFill(screen, x, y, newC=3, m =m, n=n)

for i in range(m):

  for j in range(n):

    print(screen[i][j], end = " ")
  print()

"""
ip:
screen = [[1, 1, 1, 1, 1, 1, 1, 1],  
          [1, 1, 1, 1, 1, 1, 0, 0],  
          [1, 0, 0, 1, 1, 0, 1, 1],  
          [1, 2, 2, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 2, 2, 0],  
          [1, 1, 1, 1, 1, 2, 1, 1],  
          [1, 1, 1, 1, 1, 2, 2, 1]] 

OP:

1 1 1 1 1 1 1 1 
1 1 1 1 1 1 0 0 
1 0 0 1 1 0 1 1 
1 3 3 3 3 0 1 0 
1 1 1 3 3 0 1 0 
1 1 1 3 3 3 3 0 
1 1 1 1 1 3 1 1 
1 1 1 1 1 3 3 1
"""  
