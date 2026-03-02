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


myobj=Queue(10)
myobj.printlist()
