import unittest
from src.models import Product, Category


class TestModels(unittest.TestCase):

    def test_product_initialization(self):
        product = Product(
            "Смартфон Apple iPhone 15 Plus",
            "128Gb, Dual nano SIM, Yellow",
            89990.00,
            15,
        )
        assert product.name == "Смартфон Apple iPhone 15 Plus"
        assert product.description == "128Gb, Dual nano SIM, Yellow"
        assert product.price == 89990.00
        assert product.quantity == 15
        pass

    def test_category_initialization(self):
        p1 = Product("Умная колонка Яндекс Станция Миди",
                     "Оранжевый", 10990.00, 7)
        p2 = Product(
            "Смарт-часы Apple Watch Series 9",
            "GPS, 41 мм, алюминий", 39990.00, 12
        )
        p3 = Product(
            "Беспроводные наушники Sony WH-1000XM5",
            "Черные", 29990.00, 20)
        category = Category(
            "Электроника", "Популярные устройства",
            [p1, p2, p3])
        assert category.name == "Электроника"
        assert category.description == "Популярные устройства"
        assert category.products == [p1, p2, p3]
        pass

    def test_category_count_increment(self):
        initial_count = Category.total_categories
        Category("Гаджеты", "Новинки сезона", [])
        assert Category.total_categories == initial_count + 1

    def test_product_count_increment(self):
        # Создаем продукты
        products = [
            Product(
                "Игровой ноутбук ASUS ROG Strix G16",
                "16\", Intel Core i7, 16ГБ, 512ГБ SSD",  # Исправлена кавычка
                129990.00,
                5,
            ),
            Product(
                'Телевизор Samsung Crystal UHD 4K 55"',
                "Smart TV, 2024",
                59990.00,
                8
            ),
        ]

        # Создаем категорию с продуктами
        category = Category(
            "Компьютерная техника", "Топовые модели", products)

        # Проверяем, что количество продуктов в категории соответствует ожидаемому
        assert category.total_products == len(products)


if __name__ == "__main__":
    unittest.main()
