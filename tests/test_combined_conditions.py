import io
import unittest
from unittest.mock import patch

from src.main import main


class TestCombinedConditions(unittest.TestCase):

    def test_empty_first_row(self):
        output = io.StringIO()

        with patch("src.main.input_matrix", return_value=[[]]):
            with patch("sys.stdout", output):
                main()

        self.assertIn(
            "Матрица не должна быть пустой",
            output.getvalue()
        )


if __name__ == "__main__":
    unittest.main()
