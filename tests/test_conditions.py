import unittest

from src.processing_module import find_min_max, swap_rows


class TestConditions(unittest.TestCase):

    def test_min_condition_true(self):
        matrix = [[5, 6], [1, 4]]
        self.assertEqual(find_min_max(matrix), (1, 0))

    def test_min_condition_false(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(find_min_max(matrix), (0, 1))

    def test_max_condition_true(self):
        matrix = [[1, 2], [5, 4]]
        self.assertEqual(find_min_max(matrix), (0, 1))

    def test_max_condition_false(self):
        matrix = [[5, 4], [1, 2]]
        self.assertEqual(find_min_max(matrix), (1, 0))

    def test_equal_elements(self):
        matrix = [[3, 3], [3, 3]]
        self.assertEqual(find_min_max(matrix), (0, 0))

    def test_swap_same_row(self):
        matrix = [[1, 2], [3, 4]]
        swap_rows(matrix, 0, 0)
        self.assertEqual(matrix, [[1, 2], [3, 4]])


if __name__ == "__main__":
    unittest.main()
