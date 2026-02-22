class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, values):
        self.head = None
        prev = None
        for v in values:
            node = Node(v)
            if not self.head:
                self.head = node
            else:
                prev.next = node
            prev = node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

    def reverse(self): 
        prev=None
        curr=self.head       
        while curr:
            aft=curr.next
            curr.next=prev
            prev=curr
            curr=aft
        self.head= prev
        return self.head
        
ll = LinkedList([1, 2, 3, 4, 5])
ll.print_list()
ll.reverse()
ll.print_list()