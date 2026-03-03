class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Queue:
    def __init__(self,value):
        newnode= Node(value)
        self.first=newnode
        self.last=newnode
        self.length=1



    def printlist(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next
    
    def enqueue(self,value):
        newnode=Node(value)
        if self.length==0:

            self.first=newnode
            self.last=newnode
        else:
            temp=self.last
            self.last.next=newnode
            self.last=newnode
        self.length+=1

    def dequeue(self):
        temp=self.first
        if self.length==0:
            return False
        elif self.length==1:
            self.first=None
            self.last=None

        else:
            self.first=self.first.next
            temp.next=None
            self.length-=1
        


myobj=Queue(10)
myobj.printlist()

print("--- After Enqueue --- ")
myobj.enqueue(11)
myobj.enqueue(12)
myobj.enqueue(13)
myobj.printlist()


print("--- After Dequeue --- ")
myobj.dequeue()
# myobj.dequeue()
myobj.printlist()

