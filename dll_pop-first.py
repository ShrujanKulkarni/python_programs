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
        
    def pop(self):
        temp= self.tail
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None 
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp
    def prepend(self, value):
        newnode=Node(value)
        if(self.length==0):
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode.next
            self.head=newnode
        self.length+=1
        return True
        
    def pop_first(self):
        if self.length ==0:
            self.head=None
            self.tail=None
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp
            
obj= Dll(9)
obj.append(5)
obj.append(4)

obj.printlist()
print("After pop")
obj.pop()
obj.printlist()

print("After Prepend")
obj.prepend(100)
obj.printlist()

print("After Pop first")
obj.pop_first()
obj.printlist()