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
        newnode.next=self.top
        self.top=newnode
      
    def pop(self):
        t=self.top
        self.top=self.top.next
        t.next=None
        return 1
        
myobj=Stack(10)
myobj.push(20)
myobj.push(30)
print ("After push")
myobj.printstack()
print ("after pop")
myobj.pop()
myobj.printstack()