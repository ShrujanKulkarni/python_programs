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


    def push(self,value):
        newnode=Node(value)
        if self.height==0:
            self.top=newnode
           
        else:
            newnode.next=self.top
            self.top=newnode
        self.height+=1

    def pop(self):
        if self.height==0:
            return None
        else:
            dum = self.top
            self.top=self.top.next
            dum.next=None
            self.height-=1
            return dum.value
       

obj=Stack(9)
obj.printstack()

obj.push(10)
print("----- After Push-----")
obj.printstack()

print("Popped value: ",obj.pop())
print("Popped value: ",obj.pop())
print("----- After Pop-----")
obj.printstack()



