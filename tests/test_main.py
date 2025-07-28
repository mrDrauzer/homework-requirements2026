import unittest

from src.models import Product, Category, CategoryIterator, Smartphone, LawnGrass

class TestModels(unittest.TestCase):

    def setUp(self):
        # Сброс статических счётчиков перед каждым тестом
        Category.total_categories = 0
        Category.total_products = 0

    def test_category_add_product_and_count(self):
        cat = Category("Электроника", "Раздел для техники", [])
        self.assertEqual(cat.product_count, 0)
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_products, 0)

        p = Product("Колонка", "Bluetooth", 2990, 8)
        cat.add_product(p)

        self.assertEqual(cat.product_count, 1)
        self.assertEqual(Category.total_products, 1)
        self.assertTrue(any(prod.name == "Колонка" for prod in cat.products))

    def test_category_tracker_totals(self):
        start_categories = Category.total_categories
        start_products = Category.total_products

        cat = Category("Игрушки", "Детские товары", [])
        p1 = Product("Мяч", "Футбольный", 500, 15)
        p2 = Product("Кукла", "Барби", 1200, 5)
        cat.add_product(p1)
        cat.add_product(p2)

        self.assertEqual(cat.product_count, 2)
        self.assertTrue(any(prod.name == "Кукла" for prod in cat.products))
        self.assertEqual(Category.total_categories, start_categories + 1)
        self.assertEqual(Category.total_products, start_products + 2)

        # Проверка classproperty
        self.assertEqual(Category.category_count, Category.total_categories)
        self.assertEqual(Category.product_count, Category.total_products)

    def test_product_addition(self):
        p1 = Product("Item1", "desc", 100, 2)  # 200
        p2 = Product("Item2", "desc", 50, 8)   # 400
        result = p1 + p2
        self.assertEqual(result, 600)

    def test_category_str(self):
        p1 = Product("Item1", "desc", 1500, 6)
        p2 = Product("Item2", "desc", 2500, 3)
        cat = Category("Техника", "Разное", [p1, p2])
        self.assertIn("Техника, количество продуктов: 9 шт.", str(cat))

    def test_iter_category(self):
        p1 = Product("A", "Test", 100, 2)
        p2 = Product("B", "Test", 200, 3)
        cat = Category("TestCat", "desc", [p1, p2])
        names = [p.name for p in CategoryIterator(cat)]
        self.assertListEqual(names, ["A", "B"])

    def test_product_str_repr(self):
        p = Product("Тест", "Описание", 990, 3)
        self.assertEqual(str(p), "Тест, 990 руб. Остаток: 3 шт.")
        self.assertEqual(repr(p), "Product('Тест', 'Описание', 990, 3)")

    def test_smartphone_repr(self):
        phone = Smartphone("iPhone", "Apple", 1000, 5, 90, "iPhone 15", 256, "Black")
        rep = repr(phone)
        self.assertIn("Smartphone(", rep)
        self.assertIn("iPhone", rep)

    def test_lawngrass_repr(self):
        grass = LawnGrass("Газон", "Зелёный", 500, 10, "Россия", "7 дней", "Зелёный")
        rep = repr(grass)
        self.assertIn("LawnGrass(", rep)
        self.assertIn("Россия", rep)

if __name__ == '__main__':
    unittest.main()
