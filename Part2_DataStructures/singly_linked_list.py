from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class Node:
    """Node for singly linked list."""

    data: Any
    next: Optional["Node"] = None


class SinglyLinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_head(self, data):
        """Insert new element at the head (O(1))"""
        self.head = Node(data, next=self.head)

    def delete(self, data):
        """Delete first occurrence of value (O(n))"""
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous, current = current, current.next

    def traverse(self):
        """Return list of elements (O(n))"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
