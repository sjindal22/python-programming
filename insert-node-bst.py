class Node:

  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

def insert(root, node):

  if root == None:
    root = node
  else:
    if root.val < node.val:
      if root.right == None:
        root.right = node.val
      else:
        insert(root.right, node)
    else:
      if root.left == None:
        root.left = node
      else:
        insert(root.left, node)

def printTree(root):
  
  if root:
    printTree(root.left)
    print(root.val)
    printTree(root.right)

r = Node(50)
insert(r, Node(30))
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

printTree(r)

    
