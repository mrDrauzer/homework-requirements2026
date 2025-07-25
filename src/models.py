class Product:
    """
    Класс для представления товара
    """
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.__price}, Quantity: {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    @property
    def price(self):
        """Геттер для приватного атрибута __price"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для приватного атрибута __price с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirmation = input(
                f"Вы уверены, что хотите снизить цену с {self.__price} до {new_price}? (y/n): "
            )
            if confirmation.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания продукта из словаря"""
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"]
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented


class Category:
    """
    Класс для представления категории товаров
    """
    total_products = 0
    total_categories = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []  # приватный список товаров
        self.product_count = len(self.__products)  # индивидуальный счетчик
        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def add_product(self, product):
        """Добавление продукта в категорию и обновление счетчика"""
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count = len(self.__products)
            Category.total_products += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """
        Возвращает список объектов продуктов.
        """
        return self.__products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    def __init__(self, category):
        self._products = category.products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration
