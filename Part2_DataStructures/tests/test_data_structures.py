import unittest
from Part2_DataStructures.array_and_matrix import Array
from Part2_DataStructures.stack_and_queue import Stack, Queue
from Part2_DataStructures.singly_linked_list import SinglyLinkedList
from Part2_DataStructures.rooted_tree import TreeNode


class TestArray(unittest.TestCase):
    """Unit tests for the Array data structure."""

    def setUp(self):
        """Initialize a new Array before each test."""
        self.array = Array()

    def test_insert_and_access_element(self):
        """Test inserting and accessing an element."""
        self.array.insert(10)
        self.assertEqual(self.array.access(0), 10, "Accessed value should be 10")

    def test_delete_element(self):
        """Test deleting an existing element."""
        self.array.insert(20)
        self.array.delete(20)
        self.assertNotIn(20, self.array.data, "Deleted value should not be present")

    def test_access_out_of_bounds_raises(self):
        """Test accessing an invalid index raises IndexError."""
        with self.assertRaises(IndexError):
            self.array.access(5)


class TestStack(unittest.TestCase):
    """Unit tests for the Stack data structure."""

    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        """Test pushing to and popping from the stack."""
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1, "Popped value should match pushed value")

    def test_peek_value(self):
        """Test peeking the top value."""
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2, "Peeked value should be 2")

    def test_pop_from_empty_stack_raises(self):
        """Test popping from an empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.pop()


class TestQueue(unittest.TestCase):
    """Unit tests for the Queue data structure."""

    def setUp(self):
        self.queue = Queue()

    def test_enqueue_and_dequeue(self):
        """Test enqueuing and dequeuing an element."""
        self.queue.enqueue(5)
        self.assertEqual(
            self.queue.dequeue(), 5, "Dequeued value should match enqueued value"
        )

    def test_peek_value(self):
        """Test peeking the front value."""
        self.queue.enqueue(7)
        self.assertEqual(self.queue.peek(), 7, "Peeked value should be 7")

    def test_dequeue_from_empty_queue_raises(self):
        """Test dequeuing from an empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()


class TestSinglyLinkedList(unittest.TestCase):
    """Unit tests for the SinglyLinkedList data structure."""

    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_insert_and_traverse(self):
        """Test inserting elements at head and traversing the list."""
        self.linked_list.insert_at_head(3)
        self.linked_list.insert_at_head(5)
        self.assertEqual(
            self.linked_list.traverse(), [5, 3], "Traverse result should be [5, 3]"
        )

    def test_delete_node(self):
        """Test deleting a node by value."""
        self.linked_list.insert_at_head(3)
        self.linked_list.insert_at_head(5)
        self.linked_list.delete(5)
        self.assertEqual(
            self.linked_list.traverse(), [3], "After deleting 5, list should be [3]"
        )


class TestRootedTree(unittest.TestCase):
    """Unit tests for the TreeNode class."""

    def setUp(self):
        self.root = TreeNode("Root")
        self.child1 = TreeNode("Child1")
        self.child2 = TreeNode("Child2")
        self.root.add_child(self.child1)
        self.root.add_child(self.child2)

    def test_add_child_nodes(self):
        """Test adding child nodes to a root."""
        self.assertIn(
            self.child1, self.root.children, "Child1 should be in root's children"
        )
        self.assertIn(
            self.child2, self.root.children, "Child2 should be in root's children"
        )

    def test_remove_child_node(self):
        """Test removing a child node."""
        self.root.remove_child(self.child1)
        self.assertNotIn(
            self.child1, self.root.children, "Child1 should have been removed"
        )

    def test_tree_traversal(self):
        """Test tree traversal result."""
        sub_child = TreeNode("SubChild")
        self.child1.add_child(sub_child)
        expected_traversal = ["Root", "Child1", "SubChild", "Child2"]
        self.assertEqual(
            self.root.traverse(),
            expected_traversal,
            "Traversal result should match expected order",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
