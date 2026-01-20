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

    def append(self,value):
        newnode= Node(value)
        if self.length==0:
            self.head=newnode
            self.tail=newnode
            self.length+=1
        else:
            self.tail.next=newnode
            self.tail=newnode
        return True

ll=LinkedList(10)
ll.printlist()
print("----- After Append -----")
ll.append(11)
ll.append(12)
ll.append(13)
ll.append(14)
ll.printlist()


