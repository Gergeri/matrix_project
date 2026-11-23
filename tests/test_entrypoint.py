import io
import runpy
import unittest
from unittest.mock import patch


class TestEntrypoint(unittest.TestCase):

    def test_direct_execution(self):
        output = io.StringIO()
        values = ["1", "1", "5", "нет"]

        with patch("builtins.input", side_effect=values):
            with patch("sys.stdout", output):
                runpy.run_module("src.main", run_name="__main__")

        self.assertIn("Исходная матрица:", output.getvalue())
        self.assertIn("Матрица после перестановки строк:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
