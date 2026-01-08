class Node:
    def __init__(self,value):
        self.value= value
        self.next= None

class Linkedlist:
    def __init__(self,value):
        self.length=0
        newnode=Node(value)
        self.head=newnode
        self.tail=newnode
        self.length+=1
        # return newnode

def printlist(self):
    temp= self.head
    while(temp):
        print(temp.value)
        temp=temp.next

mylinkedlist = Linkedlist(10)
print(mylinkedlist.head.value)