class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self,value):
        newnode=Node(value)
        self.head=newnode
        self.tail=newnode
        self.length=1

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next


ll=LinkedList(10)
ll.printlist()