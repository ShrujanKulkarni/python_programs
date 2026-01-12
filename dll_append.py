class Node:
    def __init__(self,value):
        self.value= value
        self.next= None
        self.prev= None
class Dll:
    def __init__(self,value):
        newnode=Node(value)
        self.head=newnode
        self.tail=newnode
        self.length=1
        
        
    def printlist(self):
        temp=self.head
        while(temp is not None):
            print(temp.value)
            temp=temp.next
            
            
    def append(self,value):
        newnode=Node(value)
        if self.tail==None:
            self.tail=newnode
            self.head=newnode
        else:
            self.tail.next= newnode
            newnode.prev=self.tail
            self.tail=newnode
        self.length+=1
            
obj= Dll(9)
obj.append(5)
obj.append(4)

obj.printlist()