import io
import unittest
from unittest.mock import patch

from src.main import main


class TestMainFlow(unittest.TestCase):

    def test_repeat_yes(self):
        matrices = [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]]
        ]

        output = io.StringIO()

        with patch("src.main.input_matrix", side_effect=matrices):
            with patch("builtins.input", side_effect=["да", "нет"]):
                with patch("sys.stdout", output):
                    main()

        self.assertEqual(
            output.getvalue().count("Исходная матрица:"), 2
        )

    def test_repeat_no(self):
        matrix = [[1, 2], [3, 4]]
        output = io.StringIO()

        with patch("src.main.input_matrix", return_value=matrix):
            with patch("builtins.input", return_value="нет"):
                with patch("sys.stdout", output):
                    main()

        self.assertEqual(
            output.getvalue().count("Исходная матрица:"), 1
        )


if __name__ == "__main__":
    unittest.main()
