
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

# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.

    def contains(self, value):
        runner = self.head
        while runner != None:
            if runner.value == value:
                return True
            runner = runner.next
        return False

    # Create a new SLL method length() that returns number of nodes in that list.
    def length(self):
        count = 0
        runner = self.head
        while runner != None:
            count += 1
            runner = runner.next
        print(count)
        return self
        
    # Create display() that returns a string containing all list values. Build what you wish console.log(myList) did!

    def display(self):
        if self.head == None:
            print("No values")
        else:
            runner = self.head
            myList = ""
            while runner != None:
                myList += str(runner.value) + ", "
                print(myList)
                runner = runner.next
        return self

sll = SLL()
sll.addFront(4)
sll.addFront(8)
sll.addFront(2)
sll.addFront(6)

print(sll.contains(7))
sll.length()
sll.display()

