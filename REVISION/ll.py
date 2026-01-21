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
        # print(f"Number of nodes={self.length}")

    def append(self,value):
        newnode= Node(value)
        if self.length==0:
            self.head=newnode
            self.tail=newnode
            self.length+=1
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.length+=1
        return True

    def reverse(self):
        bef= None
        curr =self.head

        while curr:
            aft=curr.next
            curr.next=bef
            bef=curr
            curr=aft
        self.head = bef
        return self.head


    def remove(self,x):
        dummy=Node(0)
        dummy.next=None

        prev=dummy
        dummy.next=self.head
        curr=self.head

        while curr:
            if curr.value!=x:
                prev=curr
                curr=curr.next
            else:
                prev.next=curr.next
                curr=curr.next
        return dummy.next


if __name__ == "__main__":
    ll=LinkedList(10)
    # ll.printlist()
    # print("----- After Append -----")
    ll.append(11)
    ll.append(12)
    ll.append(13)
    ll.append(14)
    ll.append(15)
    ll.append(16)
    ll.printlist()

    # print("----- After reverse -----")
    # ll.reverse()
    # ll.printlist()


    print("----- After remove -----")
    ll.remove(13)
    ll.printlist()




