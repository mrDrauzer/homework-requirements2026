import unittest
import json
import tempfile
import os
from src.loader import load_data_from_json
from src.models import Product  # нужен для теста str/repr

class TestLoader(unittest.TestCase):
    def setUp(self):
        """
        Подготовка временного JSON-файла с правильной структурой
        """
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
                            "quantity": 5
                        }
                    ]
                }
            ]
        }

        self.temp_file = tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".json", encoding="utf-8"
        )
        json.dump(self.test_data, self.temp_file, ensure_ascii=False, indent=2)
        self.temp_file.close()

    def tearDown(self):
        """
        Удаление временного JSON-файла после теста
        """
        os.unlink(self.temp_file.name)

    def test_load_data_from_json(self):
        """
        Проверка корректности загрузки категории и товаров
        """
        categories = load_data_from_json(self.temp_file.name)
        self.assertEqual(len(categories), 1)

        category = categories[0]
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test category description")

        # Проверяем: геттер `products` возвращает правильно отформатированную строку
        self.assertIn("Test Product", category.products)
        self.assertIn("100 руб.", category.products)
        self.assertIn("Остаток: 5 шт.", category.products)

    def test_product_str_repr(self):
        """
        Проверка __str__ и __repr__ у продукта
        """
        p = Product("Тест", "Описание", 990, 3)
        self.assertIn("Product:", str(p))
        self.assertIn("Product(", repr(p))

if __name__ == "__main__":
    unittest.main()
