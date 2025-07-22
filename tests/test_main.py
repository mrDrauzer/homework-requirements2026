import unittest
import builtins
from src.models import Product, Category


class TestModels(unittest.TestCase):

    def test_product_initialization(self):
        product = Product("Ноутбук", "Модель 2023", 59990.0, 10)
        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.description, "Модель 2023")
        self.assertEqual(product.price, 59990.0)
        self.assertEqual(product.quantity, 10)

    def test_product_setter_validation(self):
        product = Product("Товар", "Описание", 1000, 5)
        product.price = -100  # не должен принять
        self.assertEqual(product.price, 1000)

    def test_product_price_reduction_declined(self):
        p = Product("X", "Desc", 5000, 5)
        original_input = builtins.input
        builtins.input = lambda _: "n"  # эмуляция отказа
        p.price = 3000  # попытка понижения
        builtins.input = original_input
        self.assertEqual(p.price, 5000)  # цена осталась прежней

    def test_new_product_creation(self):
        data = {"name": "Test", "description": "Desc", "price": 2000, "quantity": 3}
        p = Product.new_product(data)
        self.assertEqual(p.name, "Test")
        self.assertEqual(p.price, 2000)
        self.assertEqual(p.quantity, 3)

    def test_category_add_product_and_count(self):
        cat = Category("Электроника", "Раздел для техники", [])
        self.assertEqual(cat.product_count, 0)
        p = Product("Колонка", "Bluetooth", 2990, 8)
        cat.add_product(p)
        self.assertEqual(cat.product_count, 1)
        self.assertIn("Колонка", cat.products)  # products — теперь геттер: строка

    def test_category_tracker_totals(self):
        start_total_categories = Category.total_categories
        start_total_products = Category.total_products

        category = Category("Игрушки", "Детские товары", [])
        prod1 = Product("Мяч", "Футбольный", 500, 15)
        prod2 = Product("Кукла", "Барби", 1200, 5)

        category.add_product(prod1)
        category.add_product(prod2)

        self.assertEqual(category.product_count, 2)
        self.assertTrue("Кукла" in category.products)
        self.assertEqual(Category.total_categories, start_total_categories + 1)
        self.assertEqual(Category.total_products, start_total_products + 2)

    def test_product_str_repr(self):
        p = Product("Тест", "Описание", 990, 3)
        self.assertIn("Product:", str(p))
        self.assertIn("Product(", repr(p))


if __name__ == "__main__":
    unittest.main()
