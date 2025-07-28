import unittest
import tempfile
import json
import os

from src.loader import load_data_from_json
from src.models import Product, Category

class TestLoader(unittest.TestCase):

    def setUp(self):
        # Корректные данные для успешной загрузки
        self.sample_data = [
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

        # Создаем временный JSON-файл с корректными данными
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix=".json")
        json.dump(self.sample_data, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_load_data_from_json(self):
        categories = load_data_from_json(self.temp_file.name)
        self.assertEqual(len(categories), 1)
        category = categories[0]
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test category description")
        self.assertEqual(len(category.products), 1)
        product = category.products[0]
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.quantity, 5)

    def test_product_str_repr(self):
        product = Product("Тест", "Описание", 990, 3)
        self.assertEqual(str(product), "Тест, 990 руб. Остаток: 3 шт.")
        self.assertEqual(repr(product), "Product('Тест', 'Описание', 990, 3)")

    def test_load_data_from_json_skips_zero_quantity(self):
        # Данные содержат один корректный товар и один с quantity=0, который должен быть пропущен
        bad_data = [
            {
                "name": "Bad Category",
                "description": "Категория с продуктом 0 кол-ва",
                "products": [
                    {
                        "name": "Good Product",
                        "description": "Корректный товар",
                        "price": 100,
                        "quantity": 1
                    },
                    {
                        "name": "Bad Product",
                        "description": "Ошибка количество",
                        "price": 100,
                        "quantity": 0
                    }
                ]
            }
        ]

        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix=".json") as bad_file:
            json.dump(bad_data, bad_file)
            bad_file.flush()
            bad_file_path = bad_file.name

        try:
            categories = load_data_from_json(bad_file_path)
            self.assertEqual(len(categories), 1)
            category = categories[0]

            self.assertEqual(category.name, "Bad Category")
            # Проверяем, что в категории остался только корректный товар
            self.assertEqual(len(category.products), 1)
            self.assertEqual(category.products[0].name, "Good Product")

        finally:
            os.unlink(bad_file_path)


if __name__ == '__main__':
    unittest.main()
