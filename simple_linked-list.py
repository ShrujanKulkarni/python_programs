class Node:
    def __init__(self,value):
        self.value= value
        self.next=None
def buildlist(values):
    head=tail=None
    for v in values:
        newnode= Node(v)
        if head==None:
            head=tail=newnode
        else:
            tail.next=newnode
            tail=newnode
    return head
    
def printlist(head):
    temp= head
    while(temp):
        print(temp.value)
        temp=temp.next
   
data= buildlist([10,20,30,40])
printlist(data)