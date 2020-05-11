class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def convert(nums):

  if not nums:
    return None

  else:
    mid = len(nums) // 2

    root = Node(nums[mid])
    root.left = convert(nums[:mid])
    root.right = convert(nums[mid+1:])

  return root

print(convert([-10,-3,0,5,9]))
