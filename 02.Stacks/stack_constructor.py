class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Stack:
    def __init__(self,value):
        newnode=Node(value)
        self.top=newnode
        self.height=1

    def printstack(self):
        temp=self.top
        while(temp):
            print(temp.value)
            temp=temp.next


obj=Stack(9)
obj.printstack()