class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self,head=None):
        self.head=None
    def traverse(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
    def swapNodes(self, x, y): 
        if x == y: 
            return 
        prevX = None
        currX = self.head 
        while currX != None and currX.data != x: 
            prevX = currX 
            currX = currX.next
        prevY = None
        currY = self.head 
        while currY != None and currY.data != y: 
            prevY = currY 
            currY = currY.next
        if currX == None or currY == None: 
            return 
        if prevX != None: 
            prevX.next = currY 
        else:
            self.head = currY 
        if prevY != None: 
            prevY.next = currX 
        else: 
            self.head = currX 
        temp = currX.next
        currX.next = currY.next
        currY.next = temp 
    def push(self, new_data): 
        new_Node = self.Node(new_data) 
        new_Node.next = self.head 
        self.head = new_Node 
  

l=linkedlist()
l.head=node(10)
a=node(20)
b=node(30)
c=node(40)
l.head.next=a
a.next=b
b.next=c
print("Linked List")
l.traverse()
l.swapNodes(20,30)
print("After swapping 20 and 30")
l.traverse()
#l.swapNodes(10,40)
print("After swapping 10 and 40")
#l.traverse()
