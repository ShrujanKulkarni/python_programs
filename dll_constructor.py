class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        newnode=Node(value)
        self.head=newnode
        self.tail=newnode
        self.length=1

    def printlist(self):
        curr=self.head
        while curr is not None:
            print(curr.value)
            curr=curr.next

dll=DoublyLinkedList(9)
dll.printlist()