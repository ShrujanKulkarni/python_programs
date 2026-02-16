class Node:
    def __init__(self,value):
        self.value= value
        self.next=None

class Linkedlist:
    def __init__(self,value):
        newnode=Node(value)
        self.head=newnode
        self.tail=newnode
        self.height=1

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
        print(f"Length= {self.height}")


    def append(self,value):
        if self.height==0:
            newnode=Node(value)
            self.head=newnode
            self.tail=newnode
            self.height=1            
        else:
            newnode=Node(value)
            self.tail.next=newnode
            self.tail=newnode
            

myobj=Linkedlist(10)
myobj.printlist()