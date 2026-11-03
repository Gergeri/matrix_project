
import unittest
from src.processing_module import find_min_max, swap_rows


class TestMatrix(unittest.TestCase):

    def test_swap_rows(self):
        matrix = [[1, 2], [3, 4]]
        min_row, max_row = find_min_max(matrix)
        swap_rows(matrix, max_row, min_row)
        self.assertEqual(matrix, [[3, 4], [1, 2]])

    def test_same_row(self):
        matrix = [[1, 5]]
        min_row, max_row = find_min_max(matrix)
        swap_rows(matrix, max_row, min_row)
        self.assertEqual(matrix, [[1, 5]])

    def test_negative_numbers(self):
        matrix = [[-10, 2], [3, 8]]
        min_row, max_row = find_min_max(matrix)
        swap_rows(matrix, max_row, min_row)
        self.assertEqual(matrix, [[3, 8], [-10, 2]])


if __name__ == "__main__":
    unittest.main()
