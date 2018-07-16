class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class Slist:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    
    def addNode(self, value):
        node = Node(value)
        run = self.head
        while(run.next != None):
            run = run.next
        run.next = node
        while(run.next == None):
            run = None
     
    def printAllValues(self, msg=""):
        run = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(run.next != None):
            print(id(run), run.value, id(run.next))
            run = run.next        
        print(id(run), run.value, id(run.next))

    def delNode(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = None
        run = self.head
        while (run != None):
            if (value == run.value and prev != None):
                prev.next = run.next
                return run.value    
            prev = run
            run = run.next




list = Slist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.delNode(7) # removes 9, which is one of the middle nodes in the list
list.delNode(5) # removes 5, which is the first value in the list
list.delNode(1) # removes 1, which is the last node in the list
list.printAllValues("Attempt 1")
      

