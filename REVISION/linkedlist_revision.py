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
        # print("Length:",self.length)

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
        
    def reverse(self):
 
        prev=None
        curr= self.head
        while(curr):
             aft=curr.next
             curr.next=prev
             prev=curr
             curr=aft
        self.head=prev

    def remove(self,index):
        curr=self.head
        temp=self.head

        while(temp.value!=index):
            curr=temp
            temp=temp.next             

        curr.next=temp.next
        temp.next=None
        self.length-=1


    def middle(self):
         s=f=self.head

         while f.next and f.next.next:
             s=s.next
             f=f.next.next
         return s.value


ob= Linkedlist(10)
# ob.printlist()
print("After append")
ob.append(11)
ob.append(12)
ob.append(13)
ob.append(14)
ob.append(15)
ob.append(16)
ob.append(17)
ob.append(18)


ob.printlist()

# print("Popped value ",ob.pop())
# ob.printlist()

# print("After reverse:")
# ob.reverse()
# ob.printlist()

# print("After removal by value:")
# ob.remove(11)
# ob.printlist()

print("Middle of linkedlist is:", ob.middle())