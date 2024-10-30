import unittest
import importlib

from task import verify_libraries


class TestCase(unittest.TestCase):
    def test_verify_libraries(self):
        self.assertTrue(verify_libraries, msg="verify all libraries are installed successfully")

    def test_matplotlib(self):
        try:
            importlib.import_module("matplotlib")
        except ImportError:
            self.fail("matplotlib is not installed")

    def test_ploty(self):
        try:
            importlib.import_module("plotly")
        except ImportError:
            self.fail("plotly is not installed")

    def test_pandas(self):
        try:
            importlib.import_module("pandas")
        except ImportError:
            self.fail("pandas is not installed")
