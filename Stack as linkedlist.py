#Stack as Linked List
class Node:
    def __init__(self,val=None):
        self.data=val
        self.next=None
class Stack:
    def __init__(self,root=None):
        self.root=None
    def push(self,item):
        item=Node(item)
        item.next=self.root
        self.root=item
        return self.root
    def isEmpty(self):
        return self.root is None
    def pop(self):
        if self.isEmpty is True:
            return "Empty"
        temp=self.root
        self.root=self.root.next
        popped=temp.data 
        return popped
    def peek(self):
        if self.isEmpty is True:
            return "Empty"
        return self.root.data
    def printl(self):
        temp=self.root
        while temp.next is not None:
            print(temp.data,end="->")
            temp=temp.next
s=Stack()
for i in range(10):
    s.push(i*10)
print("\n")
s.printl()
print("\n Popped element is",s.pop())
print("\n Popped element is",s.pop())
print("\n Peek element is:",s.peek())