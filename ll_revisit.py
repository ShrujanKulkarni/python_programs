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
        # print(f"Length= {self.height}")


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
            self.height+=1

    def pop(self):
        if self.height==0:
            print("No item to be popped")
            return
        else:
            p=None
            t = self.head
            while t.next:
                p=t
                t=t.next
            p.next=None
            self.tail=p
            self.height-=1

    def reverse(self):
        bef=None
        curr= self.head
        while curr:
            aft=curr.next
            curr.next=bef
            bef=curr
            curr=aft
        self.head=bef




myobj=Linkedlist(10)
# myobj.printlist()

print("---- Added Append----")
myobj.append(11)
myobj.append(12)
myobj.append(13)
myobj.printlist()
# 

# print("---- Added Pop----")
# myobj.pop()
# myobj.printlist()


print("---- after Reverse ---- ")
myobj.reverse()
myobj.printlist()


