class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    p1, p2 = l1.head, l2.head

    while p1 and p2:
        if p1.value < p2.value:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    # Attach remaining nodes
    tail.next = p1 if p1 else p2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list
