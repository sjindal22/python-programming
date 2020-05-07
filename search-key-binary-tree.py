def binarySearchTree(root, key):

  if root == None or root.val == key:
    return root

  elif root.val > key:
    return search(root.left, key)
  
  return search(root.right, key)

