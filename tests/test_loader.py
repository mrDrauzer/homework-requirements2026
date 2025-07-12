import unittest
import json
import tempfile
import os
from src.loader import load_data_from_json


class TestLoader(unittest.TestCase):

    def setUp(self):
        """Создание тестового JSON-файла"""
        self.test_data = {
            "categories": [
                {
                    "name": "Test Category",
                    "description": "Test category description",
                    "products": [
                        {
                            "name": "Test Product",
                            "description": "Test product description",
                            "price": 100,
                            "quantity": 5,
                        }
                    ],
                }
            ]
        }

        # Создание временного файла с правильной кодировкой
        self.temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            suffix=".json",
            encoding="utf-8",  # Добавить явное указание кодировки
        )
        json.dump(self.test_data, self.temp_file, ensure_ascii=False, indent=2)
        self.temp_file.close()

    def tearDown(self):
        """Удаление временного файла"""
        os.unlink(self.temp_file.name)

    def test_load_data_from_json(self):
        """Тест загрузки данных из JSON"""
        categories = load_data_from_json(self.temp_file.name)

        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, "Test Category")
        self.assertEqual(len(categories[0].products), 1)
        self.assertEqual(categories[0].products[0].name, "Test Product")
        self.assertEqual(categories[0].products[0].price, 100)


if __name__ == "__main__":
    unittest.main()
