# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.

class Node:
    def __init__(self, value):
        self.value = value 
        self.next= None 

class SLL:
    def __init__(self):
        self.head = None

    def addFront(self, value):
        new_node = Node(value)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node
        return self

    def printVals(self):
        if self.head == None:
            print("Linked list is empty")
            return

        llstr = ""

        while self.head != None:
            llstr += str(self.head.value)
            self.head = self.head.next
            return llstr
        print(llstr)


sll = SLL()
sll.addFront(4)
sll.addFront(8)
sll.addFront(2)
sll.addFront(6)

sll.printVals()
# sll.contains(4)

