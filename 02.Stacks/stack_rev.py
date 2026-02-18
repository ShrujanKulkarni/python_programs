class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self,value):
        newnode=Node(value)
        self.top=newnode
        self.len=1
        
    def printstack(self):
        t=self.top
        while t:
            print(t.value)
            t=t.next
    def push(self, value):
        newnode=Node(value)
myobj=Stack(10)
myobj.printstack()