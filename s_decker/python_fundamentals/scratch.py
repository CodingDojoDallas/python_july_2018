# New Node
class SLNode:
 def __init__(self, value):
  self.value = value
  self.next = None


  # SList class
  class SList:
 def __init__(self):
  self.head = None
  self.tail = None

# Code
list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')


list = Slist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(9) # removes 9, which is one of the middle nodes in the list
list.removeNode(5) # removes 5, which is the first value in the list
list.removeNode(1) # removes 1, which is the last node in the list
list.printAllValues("Attempt 1")