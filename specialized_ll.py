"""
==============================================================================
COMPREHENSIVE LINKED LIST IMPLEMENTATION LIBRARY
==============================================================================
A complete implementation of various linked list data structures and algorithms
Including: Singly Linked List, Doubly Linked List, Circular Linked List
With extensive test cases and demonstration programs
==============================================================================
"""

import sys
import time
import random
from typing import Any, Optional, List, Callable
from dataclasses import dataclass
from enum import Enum

# ==============================================================================
# SECTION 1: BASE NODE CLASSES
# ==============================================================================

class Node:
    """Basic node for singly linked list"""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None
    
    def __repr__(self):
        return f"Node({self.value})"
    
    def __str__(self):
        return str(self.value)


class DoublyNode:
    """Node for doubly linked list with prev and next pointers"""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['DoublyNode'] = None
        self.prev: Optional['DoublyNode'] = None
    
    def __repr__(self):
        return f"DoublyNode({self.value})"
    
    def __str__(self):
        return str(self.value)


# ==============================================================================
# SECTION 2: SINGLY LINKED LIST IMPLEMENTATION
# ==============================================================================

class SinglyLinkedList:
    """
    Complete implementation of Singly Linked List with all common operations
    """
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length: int = 0
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return f"SinglyLinkedList(length={self.length})"
    
    def __str__(self):
        if not self.head:
            return "Empty List"
        
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"
    
    def is_empty(self) -> bool:
        """Check if list is empty"""
        return self.head is None
    
    def append(self, value: Any) -> None:
        """Add element to the end of the list"""
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def prepend(self, value: Any) -> None:
        """Add element to the beginning of the list"""
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
    
    def insert(self, index: int, value: Any) -> bool:
        """Insert element at specific index"""
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(value)
            return True
        
        if index == self.length:
            self.append(value)
            return True
        
        new_node = Node(value)
        current = self.head
        
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return True
    
    def delete_first(self) -> Optional[Any]:
        """Remove and return first element"""
        if not self.head:
            return None
        
        value = self.head.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        self.length -= 1
        return value
    
    def delete_last(self) -> Optional[Any]:
        """Remove and return last element"""
        if not self.head:
            return None
        
        value = self.tail.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            
            current.next = None
            self.tail = current
        
        self.length -= 1
        return value
    
    def delete_at(self, index: int) -> Optional[Any]:
        """Delete element at specific index"""
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.delete_first()
        
        if index == self.length - 1:
            return self.delete_last()
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        value = current.next.value
        current.next = current.next.next
        self.length -= 1
        return value
    
    def search(self, value: Any) -> int:
        """Find index of value, return -1 if not found"""
        current = self.head
        index = 0
        
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, index: int) -> Optional[Any]:
        """Get value at specific index"""
        if index < 0 or index >= self.length:
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.value
    
    def set(self, index: int, value: Any) -> bool:
        """Set value at specific index"""
        if index < 0 or index >= self.length:
            return False
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.value = value
        return True
    
    def reverse(self) -> None:
        """Reverse the linked list in place"""
        if not self.head or not self.head.next:
            return
        
        self.tail = self.head
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def reverse_recursive(self, node: Optional[Node] = None) -> Optional[Node]:
        """Reverse list recursively"""
        if node is None:
            node = self.head
        
        if not node or not node.next:
            self.head = node
            return node
        
        reversed_head = self.reverse_recursive(node.next)
        node.next.next = node
        node.next = None
        
        return reversed_head
    
    def find_middle(self) -> Optional[Any]:
        """Find middle element using slow-fast pointer technique"""
        if not self.head:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.value
    
    def has_cycle(self) -> bool:
        """Detect cycle using Floyd's algorithm"""
        if not self.head:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def remove_duplicates(self) -> None:
        """Remove duplicate values from sorted list"""
        if not self.head:
            return
        
        current = self.head
        
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
                self.length -= 1
            else:
                current = current.next
    
    def remove_duplicates_unsorted(self) -> None:
        """Remove duplicates from unsorted list using set"""
        if not self.head:
            return
        
        seen = set()
        current = self.head
        seen.add(current.value)
        
        while current.next:
            if current.next.value in seen:
                current.next = current.next.next
                self.length -= 1
            else:
                seen.add(current.next.value)
                current = current.next
    
    def partition_list(self, x: Any) -> None:
        """Partition list around value x"""
        d1 = Node(0)
        d2 = Node(0)
        p1 = d1
        p2 = d2
        curr = self.head
        
        while curr is not None:
            if curr.value < x:
                p1.next = curr
                p1 = p1.next
            else:
                p2.next = curr
                p2 = p2.next
            curr = curr.next
        
        p2.next = None
        p1.next = d2.next
        self.head = d1.next
    
    def merge_sorted(self, other: 'SinglyLinkedList') -> 'SinglyLinkedList':
        """Merge two sorted linked lists"""
        result = SinglyLinkedList()
        dummy = Node(0)
        current = dummy
        
        p1 = self.head
        p2 = other.head
        
        while p1 and p2:
            if p1.value <= p2.value:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        if p1:
            current.next = p1
        if p2:
            current.next = p2
        
        result.head = dummy.next
        
        current = result.head
        while current:
            result.length += 1
            if not current.next:
                result.tail = current
            current = current.next
        
        return result
    
    def to_list(self) -> List[Any]:
        """Convert linked list to Python list"""
        result = []
        current = self.head
        
        while current:
            result.append(current.value)
            current = current.next
        
        return result
    
    def from_list(self, items: List[Any]) -> None:
        """Create linked list from Python list"""
        self.head = None
        self.tail = None
        self.length = 0
        
        for item in items:
            self.append(item)
    
    def clear(self) -> None:
        """Clear all elements from list"""
        self.head = None
        self.tail = None
        self.length = 0


# ==============================================================================
# SECTION 3: DOUBLY LINKED LIST IMPLEMENTATION
# ==============================================================================

class DoublyLinkedList:
    """
    Complete implementation of Doubly Linked List with bidirectional traversal
    """
    
    def __init__(self):
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self.length: int = 0
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return f"DoublyLinkedList(length={self.length})"
    
    def __str__(self):
        if not self.head:
            return "Empty List"
        
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "None <-> " + " <-> ".join(values) + " <-> None"
    
    def is_empty(self) -> bool:
        """Check if list is empty"""
        return self.head is None
    
    def append(self, value: Any) -> None:
        """Add element to end"""
        new_node = DoublyNode(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def prepend(self, value: Any) -> None:
        """Add element to beginning"""
        new_node = DoublyNode(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
    
    def insert(self, index: int, value: Any) -> bool:
        """Insert at specific index"""
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(value)
            return True
        
        if index == self.length:
            self.append(value)
            return True
        
        new_node = DoublyNode(value)
        
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.prev
        
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        
        self.length += 1
        return True
    
    def delete_first(self) -> Optional[Any]:
        """Remove and return first element"""
        if not self.head:
            return None
        
        value = self.head.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return value
    
    def delete_last(self) -> Optional[Any]:
        """Remove and return last element"""
        if not self.tail:
            return None
        
        value = self.tail.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.length -= 1
        return value
    
    def delete_at(self, index: int) -> Optional[Any]:
        """Delete element at index"""
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.delete_first()
        
        if index == self.length - 1:
            return self.delete_last()
        
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.prev
        
        value = current.value
        current.prev.next = current.next
        current.next.prev = current.prev
        
        self.length -= 1
        return value
    
    def get(self, index: int) -> Optional[Any]:
        """Get value at index"""
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.prev
        
        return current.value
    
    def reverse(self) -> None:
        """Reverse the doubly linked list"""
        if not self.head or not self.head.next:
            return
        
        current = self.head
        self.tail = self.head
        
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            
            if not temp:
                self.head = current
            
            current = temp
    
    def to_list(self) -> List[Any]:
        """Convert to Python list"""
        result = []
        current = self.head
        
        while current:
            result.append(current.value)
            current = current.next
        
        return result
    
    def to_list_reverse(self) -> List[Any]:
        """Convert to Python list in reverse order"""
        result = []
        current = self.tail
        
        while current:
            result.append(current.value)
            current = current.prev
        
        return result


# ==============================================================================
# SECTION 4: CIRCULAR LINKED LIST IMPLEMENTATION
# ==============================================================================

class CircularLinkedList:
    """
    Circular Linked List where last node points back to first
    """
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.length: int = 0
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return f"CircularLinkedList(length={self.length})"
    
    def __str__(self):
        if not self.head:
            return "Empty Circular List"
        
        values = []
        current = self.head
        first_iteration = True
        
        while current != self.head or first_iteration:
            values.append(str(current.value))
            current = current.next
            first_iteration = False
        
        return " -> ".join(values) + f" -> [back to {self.head.value}]"
    
    def append(self, value: Any) -> None:
        """Add element to end"""
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
        
        self.length += 1
    
    def prepend(self, value: Any) -> None:
        """Add element to beginning"""
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        
        self.length += 1
    
    def delete_first(self) -> Optional[Any]:
        """Remove first element"""
        if not self.head:
            return None
        
        value = self.head.value
        
        if self.length == 1:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = self.head.next
            self.head = self.head.next
        
        self.length -= 1
        return value
    
    def to_list(self) -> List[Any]:
        """Convert to Python list"""
        if not self.head:
            return []
        
        result = []
        current = self.head
        first_iteration = True
        
        while current != self.head or first_iteration:
            result.append(current.value)
            current = current.next
            first_iteration = False
        
        return result


# ==============================================================================
# SECTION 5: ADVANCED ALGORITHMS
# ==============================================================================

class LinkedListAlgorithms:
    """
    Collection of advanced algorithms for linked lists
    """
    
    @staticmethod
    def merge_k_sorted_lists(lists: List[SinglyLinkedList]) -> SinglyLinkedList:
        """Merge k sorted linked lists"""
        if not lists:
            return SinglyLinkedList()
        
        while len(lists) > 1:
            merged = []
            
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else SinglyLinkedList()
                merged.append(list1.merge_sorted(list2))
            
            lists = merged
        
        return lists[0]
    
    @staticmethod
    def add_two_numbers(l1: SinglyLinkedList, l2: SinglyLinkedList) -> SinglyLinkedList:
        """Add two numbers represented as linked lists"""
        result = SinglyLinkedList()
        carry = 0
        
        p1 = l1.head
        p2 = l2.head
        
        while p1 or p2 or carry:
            val1 = p1.value if p1 else 0
            val2 = p2.value if p2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            result.append(digit)
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        return result
    
    @staticmethod
    def is_palindrome(ll: SinglyLinkedList) -> bool:
        """Check if linked list is palindrome"""
        values = ll.to_list()
        return values == values[::-1]
    
    @staticmethod
    def intersection_point(l1: SinglyLinkedList, l2: SinglyLinkedList) -> Optional[Node]:
        """Find intersection point of two linked lists"""
        if not l1.head or not l2.head:
            return None
        
        p1 = l1.head
        p2 = l2.head
        
        while p1 != p2:
            p1 = p1.next if p1 else l2.head
            p2 = p2.next if p2 else l1.head
        
        return p1
    
    @staticmethod
    def remove_nth_from_end(ll: SinglyLinkedList, n: int) -> bool:
        """Remove nth node from end"""
        if n <= 0 or n > ll.length:
            return False
        
        index = ll.length - n
        ll.delete_at(index)
        return True
    
    @staticmethod
    def rotate_right(ll: SinglyLinkedList, k: int) -> None:
        """Rotate list to the right by k positions"""
        if not ll.head or k == 0:
            return
        
        k = k % ll.length
        if k == 0:
            return
        
        current = ll.head
        for _ in range(ll.length - k - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        
        tail = new_head
        while tail.next:
            tail = tail.next
        
        tail.next = ll.head
        ll.head = new_head
    
    @staticmethod
    def swap_pairs(ll: SinglyLinkedList) -> None:
        """Swap every two adjacent nodes"""
        if not ll.head or not ll.head.next:
            return
        
        dummy = Node(0)
        dummy.next = ll.head
        current = dummy
        
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            first.next = second.next
            second.next = first
            current.next = second
            
            current = first
        
        ll.head = dummy.next
    
    @staticmethod
    def reorder_list(ll: SinglyLinkedList) -> None:
        """Reorder list: L0->L1->...->Ln-1->Ln to L0->Ln->L1->Ln-1->..."""
        if not ll.head or not ll.head.next:
            return
        
        slow = ll.head
        fast = ll.head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        prev = None
        current = second_half
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        second_half = prev
        
        first = ll.head
        second = second_half
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2


# ==============================================================================
# SECTION 6: SPECIALIZED LINKED LISTS
# ==============================================================================

class LRUCache:
    """
    LRU Cache implementation using doubly linked list and hashmap
    """
    
    class CacheNode:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev: Optional['LRUCache.CacheNode'] = None
            self.next: Optional['LRUCache.CacheNode'] = None
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.CacheNode(0, 0)
        self.tail = self.CacheNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: 'LRUCache.CacheNode') -> None:
        """Remove node from list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: 'LRUCache.CacheNode') -> None:
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        """Get value from cache"""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        """Put key-value pair in cache"""
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = self.CacheNode(key, value)
        self._add_to_head(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
    
    def __str__(self):
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(f"({current.key}:{current.value})")
            current = current.next
        return " -> ".join(result)


class SkipListNode:
    """Node for skip list"""
    def __init__(self, value: Any, level: int):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    """
    Skip List implementation for fast search
    """
    
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipListNode(None, max_level)
        self.level = 0
    
    def _random_level(self) -> int:
        """Generate random level for new node"""
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def insert(self, value: Any) -> None:
        """Insert value into skip list"""
        update = [None] * (self.max_level + 1)
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        level = self._random_level()
        
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level
        
        new_node = SkipListNode(value, level)
        
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
    
    def search(self, value: Any) -> bool:
        """Search for value in skip list"""
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        
        current = current.forward[0]
        return current is not None and current.value == value
    
    def delete(self, value: Any) -> bool:
        """Delete value from skip list"""
        update = [None] * (self.max_level + 1)
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        if current is None or current.value != value:
            return False
        
        for i in range(self.level + 1):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]
        
        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1
        
        return True


# ==============================================================================
# SECTION 7: UTILITY FUNCTIONS
# ==============================================================================

class ListUtils:
    """Utility functions for linked lists"""
    
    @staticmethod
    def generate_random_list(size: int, min_val: int = 0, max_val: int = 100) -> SinglyLinkedList:
        """Generate random linked list"""
        ll = SinglyLinkedList()
        for _ in range(size):
            ll.append(random.randint(min_val, max_val))
        return ll
    
    @staticmethod
    def generate_sorted_list(size: int, min_val: int = 0, max_val: int = 100) -> SinglyLinkedList:
        """Generate sorted linked list"""
        ll = SinglyLinkedList()
        values = sorted([random.randint(min_val, max_val)