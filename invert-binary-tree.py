class Node:
 
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

def invertTree(root):

  if root is None:
    return None

  else:
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

def printTree(node):

  if node is None:
    return None

  print(node.data)
  if node.left:
    printTree(node.left)
  if node.right:
    printTree(node.right)
  
if __name__ == "__main__":

  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)

  printTree(root)
  print("\n")
  invertedTree = invertTree(root)

  printTree(invertedTree)

"""
1
2
4
5
3
6
7

1
2(4,5)) 3(6,7)

1
3
7
6
2
5
4

1
3(7,6,) 2(5,4)
4
"""
