import unittest
from Part1_SelectionAlgorithms.deterministic_selection import deterministic_select
from Part1_SelectionAlgorithms.randomized_selection import randomized_select


class TestSelectionAlgorithms(unittest.TestCase):

    def setUp(self):
        self.arr = [7, 10, 4, 3, 20, 15]
        self.k = 3
        self.expected = sorted(self.arr)[self.k]

    def test_deterministic_selection(self):
        result = deterministic_select(self.arr.copy(), self.k)
        self.assertEqual(result, self.expected)

    def test_randomized_selection(self):
        result = randomized_select(self.arr.copy(), self.k)
        self.assertEqual(result, self.expected)


if __name__ == "__main__":
    unittest.main()
