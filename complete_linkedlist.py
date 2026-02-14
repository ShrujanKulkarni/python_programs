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

    def append(self,value):
        newnode=Node(value)
        if self.length ==0:
            self.head=self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.length+=1

    def printlist(self):
        temp= self.head
        while(temp):
            print(temp.value,"-->", end="  ")
            temp=temp.next

    def pop(self):
        if self.length==0:
            return None
        else:
            temp=pre=self.head
            while(temp.next is not None):
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None 
            self.length-=1

            if self.length==0:
                self.head=self.tail=None
        return temp.value

mylinkedlist = Linkedlist(10)
mylinkedlist.append(20)
mylinkedlist.append(30)
# mylinkedlist.append(40)
mylinkedlist.append(40)
mylinkedlist.printlist()

print("----------After Pop()----------")
popvalue= mylinkedlist.pop()
mylinkedlist.printlist()
print(f"\nPopped values is:{popvalue}")
