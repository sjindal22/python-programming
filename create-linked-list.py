class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None

  def printList(self):
    printVal = self.head
    while printVal:
      print(printVal.data, end = " ")
      printVal = printVal.next
    print()

  def insertNode(self, newValue):
    newNode = Node(newValue)
    newNode.next = self.head
    self.head = newNode

e1 = LinkedList()
e1.head = Node(1)
e2 = Node(2)
e3 = Node(3)

e1.head.next = e2
e2.next = e3
e1.insertNode(0)

e1.printList()

