from collections import deque


class Stack:
    """LIFO stack using collections.deque"""

    def __init__(self):
        self.items = deque()

    def push(self, item):
        """Push an item onto the stack (O(1))"""
        self.items.append(item)

    def pop(self):
        """Pop the top item (O(1))"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it"""
        return self.items[-1] if self.items else None

    def is_empty(self):
        """Check if stack is empty"""
        return not self.items


class Queue:
    """FIFO queue using collections.deque"""

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add item to the end of the queue (O(1))"""
        self.items.append(item)

    def dequeue(self):
        """Remove item from front of queue (O(1))"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        """Return front item without removing"""
        return self.items[0] if self.items else None

    def is_empty(self):
        """Check if queue is empty"""
        return not self.items
