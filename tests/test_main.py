import unittest
from src.main import find_min_max, swap_rows


class TestMatrix(unittest.TestCase):

    def test_swap_rows(self):
        matrix = [[1, 2], [3, 4]]

        min_row, max_row = find_min_max(matrix)
        swap_rows(matrix, max_row, min_row)

        self.assertEqual(matrix, [[3, 4], [1, 2]])


if __name__ == "__main__":
    unittest.main()