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

    def delete_first(self, x):
     dummy = Node(0)
     dummy.next = self.head

     prev = dummy
     curr = self.head

     while curr:
        if curr.value == x:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next

     self.head = dummy.next
                
                
                
        


# Driver
ll = LinkedList([1, 2, 3, 2])
ll.print_list()
ll.delete_first(2)
ll.print_list()