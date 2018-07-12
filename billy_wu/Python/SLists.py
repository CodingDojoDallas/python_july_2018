class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Slists:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next!=None):
            runner = runner.next
        runner.next = node
        # print(node.value)
    def removeNode(self, val):
        runner = self.head
        temp = self.head
        # for i in test:
        while(runner.next!=None):
            # if i==val and i==self.head:
            if val==self.head.value:
                self.head=runner.next
                runner.next = None
                runner=self.head
                return self
            # if i==val:
            if val==runner.value:
                runner = runner.next
                temp.next = runner
                return self
            temp = runner
            runner = runner.next
        # if i==val and runner.next==None:
        if val==runner.value:
            runner=temp
            runner.next=None    
            return self
            # temp = i
        # runner = runner.next
        print("The Slist does not contain the value " + str(val))
        return self
    def insertNode(self, val, index):
        newnode = Node(val)
        runner = self.head
        temp = self.head
        if index==1:
            self.head=newnode
            runner=newnode
            runner.next = temp
            return self
        for i in range(1,index):
            if i==(index-1):
                temp = runner.next
                runner.next=newnode
                newnode.next=temp
                runner = temp
                return self
            temp = runner
            runner = runner.next
        print("The Slist does not contain the value " + str(val))
        return self
    def printAllValues(self, msg=""):
        runner = self.head
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))
test = Slists(5)
test.addNode(7)
test.addNode(9)
test.addNode(6)
test.addNode(1)
test.insertNode(2,6)
test.removeNode(9)
test.removeNode(5)
test.removeNode(1)
test.removeNode(4)
test.printAllValues("Attempt 1")