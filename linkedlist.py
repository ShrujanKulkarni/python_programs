class Node:
    def __init__(self, value):
        self.value=value
        self.next= None
        
def append(value):
    head =tail = None
    for v in value:
        newnode= Node(v)
        if head==None:
            head= tail= newnode
        else:
            tail.next= newnode
            tail=newnode
    return head

def printlist(value):
    temp= head
    while(temp):
        print(temp.value)
        temp=temp.next
        
mylist= Node(10)
mylist.append(20)
mylist.append(30)