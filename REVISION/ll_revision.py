class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
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
        print("Length:",self.length)

    def append(self,value):
        newnode=Node(value)
        if self.length==0:
                self.head=newnode
                self.tail=newnode
                self.length=1
        else:
             self.tail.next=newnode
             self.tail=newnode
             self.length+=1
    
    def pop(self):
        if self.length==0:
             return None
        else:
            temp=self.head
            pre=self.head
            while temp.next:
                  pre=temp
                  temp=temp.next
            # pre.next=None
            self.tail=pre
            self.tail.next=None

            self.length-=1
            return temp.value
        
            

              


ob= Linkedlist(10)
ob.printlist()
print("After append")
ob.append(11)
ob.append(12)
ob.printlist()

print("Popped value ",ob.pop())
ob.printlist()



