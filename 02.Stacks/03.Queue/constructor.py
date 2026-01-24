class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Queue:
    def __init__(self,value):
        newnode=Node(value)
        self.first=newnode
        self.last=newnode
        self.height=1

    def printqueue(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next

myq = Queue(9)
myq.printqueue()
