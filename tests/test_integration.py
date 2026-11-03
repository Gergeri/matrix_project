
import io
import unittest
from unittest.mock import patch

from src.input_module import input_matrix
from src.output_module import print_matrix
from src.processing_module import find_min_max, swap_rows
from src.main import main


class TestIntegration(unittest.TestCase):

    def test_input_matrix(self):
        with patch("builtins.input", side_effect=["2", "2", "1 2", "3 4"]):
            matrix = input_matrix()
        self.assertEqual(matrix, [[1.0, 2.0], [3.0, 4.0]])

    def test_invalid_dimensions(self):
        values = ["0", "2", "2", "2", "1 2", "3 4"]
        with patch("builtins.input", side_effect=values):
            matrix = input_matrix()
        self.assertEqual(matrix, [[1.0, 2.0], [3.0, 4.0]])

    def test_invalid_row(self):
        values = ["1", "2", "1", "1 2"]
        with patch("builtins.input", side_effect=values):
            matrix = input_matrix()
        self.assertEqual(matrix, [[1.0, 2.0]])

    def test_invalid_numbers(self):
        values = ["1", "2", "a b", "1 2"]
        with patch("builtins.input", side_effect=values):
            matrix = input_matrix()
        self.assertEqual(matrix, [[1.0, 2.0]])

    def test_output(self):
        output = io.StringIO()
        with patch("sys.stdout", output):
            print_matrix([[1.0, 2.0], [3.0, 4.0]])
        self.assertIn("1.0 2.0", output.getvalue())

    def test_complete_integration(self):
        values = ["2", "2", "1 2", "3 4", "нет"]
        output = io.StringIO()

        with patch("builtins.input", side_effect=values):
            with patch("sys.stdout", output):
                main()

        self.assertIn("3.0 4.0", output.getvalue())

    def test_equal_values(self):
        matrix = [[2, 2], [2, 2]]
        min_row, max_row = find_min_max(matrix)
        swap_rows(matrix, max_row, min_row)
        self.assertEqual(matrix, [[2, 2], [2, 2]])

    def test_invalid_dimension_type(self):
        values = ["abc", "1", "1", "5"]
        with patch("builtins.input", side_effect=values):
            matrix = input_matrix()
        self.assertEqual(matrix, [[5.0]])

    def test_empty_matrix_error(self):
        with patch("src.main.input_matrix", return_value=[]):
            output = io.StringIO()
            with patch("sys.stdout", output):
                main()

        self.assertIn("Матрица не должна быть пустой", output.getvalue())

    def test_processing_error(self):
        with patch("src.main.input_matrix", return_value=[[1, 2]]):
            with patch("src.main.find_min_max",
                       side_effect=ValueError("Некорректные данные")):
                output = io.StringIO()
                with patch("sys.stdout", output):
                    main()

        self.assertIn("Ошибка обработки данных", output.getvalue())


if __name__ == "__main__":
    unittest.main()
