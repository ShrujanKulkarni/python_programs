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

    def enqueue(self,value):
        newnode=Node(value)

        if self.height==0:
            self.first=newnode
            self.last=newnode
          
        else:
            self.last.next=newnode
            self.last=newnode

        self.height+=1

myq = Queue(1)
myq.printqueue()


print("After enqueue")
myq.enqueue(2)
myq.printqueue()
