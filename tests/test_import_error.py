import builtins
import runpy
import unittest
from unittest.mock import patch


class TestImportError(unittest.TestCase):

    def test_module_import_error(self):
        original_import = builtins.__import__

        def fake_import(name, *args, **kwargs):
            if name == "src.input_module":
                raise ImportError("Модуль недоступен")
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=fake_import):
            with self.assertRaises(SystemExit) as context:
                runpy.run_module("src.main", run_name="__main__")

        self.assertIn(
            "Ошибка загрузки модуля",
            str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
