import unittest
import tempfile
import json
from src.loader import load_data_from_json
from src.models import Product, Category

class TestLoader(unittest.TestCase):

    def setUp(self):
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
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix=".json")
        json.dump(self.sample_data, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        import os
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

if __name__ == '__main__':
    unittest.main()
