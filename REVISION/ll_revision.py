class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self,value):
        newnode=Node(value)
        self.head=newnode
        self.tail=newnode
        self.length=1

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.value)
            print("Length:",self.length)
            temp=temp.next

    # def append(self,value):


ob= Linkedlist(10)
ob.printlist()



