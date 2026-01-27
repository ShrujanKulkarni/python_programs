class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoLists:
    def solution(self, list1, list2):
        dummy=ListNode(0)
        d=dummy
        p1=list1
        p2=list2


        while p1 and p2:
            if p1.val<=p2.val:
                d.next=p1
                p1=p1.next
            else:
                d.next=p2
                p2=p2.next
            d=d.next

        d.next= p2 if p1 is None else p1
        return dummy.next



# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

# Test cases
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

ob = MergeTwoLists()
result = ob.solution(list1, list2)
print("Merged list:")
print_list(result)  # Should output: [1, 1, 2, 3, 4, 4]