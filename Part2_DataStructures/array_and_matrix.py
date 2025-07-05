class Array:
    """A dynamic array implementation supporting basic operations."""

    def __init__(self):
        self.data = []

    def insert(self, value):
        """Insert value at the end (O(1))"""
        self.data.append(value)

    def delete(self, value):
        """Delete first occurrence of value (O(n))"""
        try:
            self.data.remove(value)
        except ValueError:
            pass  # silently ignore if not found

    def access(self, index):
        """Access element by index (O(1))"""
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of bounds")

    def __str__(self):
        return str(self.data)
