import os
import sys


import unittest

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

yaml_file_path: str = os.path.join(BASE_DIR, 'tests', 'test_one_step.yml')

from syntax.functions import parse_yaml_file


class TestDecode(unittest.TestCase):
    def tearDown(self) -> None:
        pass


class TestParse(unittest.TestCase):
    def tearDown(self) -> None:
        pass

    def test_one_step(self):
        data = parse_yaml_file(yaml_file_path)
        self.assertIsInstance(data, dict)


class TestWrite(unittest.TestCase):
    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
