class Product:
    """Класс  для представления товара"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Category:
    """Класс для представления категории товаров"""

    total_products = 0
    total_categories = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []  # Исправлено: добавлено __
        self.total_products = len(self.__products)  # Счетчик продуктов для конкретной категории
        Category.total_categories += 1

    def add_product(self, product):
        """Добавление продукта в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            self.total_products = len(self.__products)  # Обновляем счетчик
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Геттер для получения списка продуктов"""
        return self.__products
