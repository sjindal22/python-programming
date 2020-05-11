class Node:

  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

def maxDepth(node):

   if node == None:
     return 0

   else:
     lDepth = maxDepth(node.left)
     rDepth = maxDepth(node.right)

     if (lDepth > rDepth):
       return lDepth + 1

     else:
       return rDepth + 1

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.leftright = Node(5)

print(maxDepth(tree))
