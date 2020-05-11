class Stack

  def __init__(self):
    self.q = []

  def push(self, x):
    currMin = self.getMin()
    if currMin == None or x < currMin:
      currMin = x
    self.q.append((x, currMin))

  def pop(self):
    self.q.pop()

  def top(self):
    if len(self.q) == 0:
      return
    else:
      return self.q[-1][0]

  def getMin(self):
    if len(self.q) == 0:
      return
    else:
      return self.q[-1][1]
