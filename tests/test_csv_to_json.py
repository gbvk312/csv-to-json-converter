import unittest
import os
import json
import tempfile
from csv_to_json import convert_csv_to_json

class TestCSVToJson(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.csv_path = os.path.join(self.test_dir.name, "test.csv")
        self.json_path = os.path.join(self.test_dir.name, "output.json")
        
        with open(self.csv_path, 'w', encoding='utf-8') as f:
            f.write("id,name,age\n1,Alice,30\n2,Bob,25\n")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_conversion(self):
        convert_csv_to_json(self.csv_path, self.json_path)
        self.assertTrue(os.path.exists(self.json_path))
        
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Alice')
        self.assertEqual(data[1]['age'], '25')

if __name__ == '__main__':
    unittest.main()
