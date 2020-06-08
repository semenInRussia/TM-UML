import json
import os

import unittest

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from syntax.functions import parse_yaml_file
from syntax import exceptions

class TestDecode(unittest.TestCase):
    def tearDown(self) -> None:
        pass


class TestParse(unittest.TestCase):
    yaml_file_path: str = os.path.join(BASE_DIR, 'tests', 'test_one_step.yml')
    json_file_path: str = os.path.join(BASE_DIR, 'tests', 'test_one_step.json')
    yaml_not_valid_file_path: str = os.path.join(BASE_DIR, 'tests', 'not_valid.yml')

    def tearDown(self) -> None:
        pass

    def test_one_step(self):
        data = parse_yaml_file(self.yaml_file_path)
        self.assertIsInstance(data, dict)

    def test_not_file_error(self):
        with self.assertRaises(FileNotFoundError):
            parse_yaml_file('jjjjjjjhghbfgddfvjjj')

    def test_valid_content(self):
        with open(self.json_file_path) as f:
            valid_data = json.load(f)

        data = parse_yaml_file(self.yaml_file_path)

        self.assertEqual(valid_data, data)

    def test_not_valid_content(self):
        with self.assertRaises(exceptions.NotValidFileDataError):
            parse_yaml_file(self.yaml_not_valid_file_path)

class TestWrite(unittest.TestCase):
    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
