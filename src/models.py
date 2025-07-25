class Product:
    """
    Базовый класс для представления товара
    """
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания продукта из словаря"""
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"]
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного типа (одного класса)!")
        # Для тестов: считаем total-стоимость, как в старой логике
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """
    Класс для смартфонов — наследник Product, расширен доп. атрибутами
    """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
                f"{self.efficiency}, '{self.model}', {self.memory}, '{self.color}')")


class LawnGrass(Product):
    """
    Класс для газонной травы — наследник Product, расширен доп. атрибутами
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
                f"'{self.country}', '{self.germination_period}', '{self.color}')")


class Category:
    """
    Класс для представления категории товаров
    """
    total_products = 0      # Глобальный счетчик продуктов во всех категориях
    total_categories = 0    # Счетчик всех категорий

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products else []
        self.product_count = len(self._products)
        Category.total_categories += 1
        Category.total_products += len(self._products)

    def add_product(self, product):
        """Добавление продукта (только Product или его наследники!)"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self._products.append(product)
        self.product_count = len(self._products)
        Category.total_products += 1

    @property
    def products(self):
        """Возвращает список объектов продуктов"""
        return self._products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    """Итератор для обхода товаров в категории"""
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
