from abc import ABC, abstractmethod

# Дескриптор-свойство для класса
class classproperty:
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)

class BaseProduct(ABC):
    """
    Абстрактный базовый класс для продуктов.
    """
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return
        if new_price < self._price:
            confirmation = input(
                f"Вы уверены, что хотите снизить цену с {self._price} до {new_price}? (y/n): "
            )
            if confirmation.lower() != 'y':
                print("Изменение цены отменено")
                return
        self._price = new_price

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class CreationInfoMixin:
    """
    Миксин, который выводит информацию при создании объекта
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ', '.join(str(arg) for arg in args)
        print(f"{class_name} создан с параметрами: {params}")

    def __repr__(self):
        params = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({params})"

class Product(CreationInfoMixin, BaseProduct):
    """
    Основной класс продукта
    """
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    @classmethod
    def new_product(cls, product_data):
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"]
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного типа (одного класса)!")
        return self.price * self.quantity + other.price * other.quantity

class Smartphone(Product):
    """
    Смартфон — наследуется от Product
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
    Газонная трава — наследуется от Product
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
    Класс для категорий товаров
    """
    total_products = 0  # Общее количество продуктов во всех категориях
    total_categories = 0  # Общее количество категорий

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products else []
        self.product_count = len(self._products)
        Category.total_categories += 1
        Category.total_products += len(self._products)

    @property
    def products(self):
        return self._products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self._products.append(product)
        self.product_count = len(self._products)
        Category.total_products += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @classproperty
    def category_count(cls):
        """Общее количество категорий."""
        return cls.total_categories

    @classproperty
    def product_count(cls):
        """Общее количество продуктов во всех категориях."""
        return cls.total_products

    def middle_price(self):
        try:
            return sum([product.price for product in self.products]) / len(self.products)
        except ZeroDivisionError:
            return 0

class CategoryIterator:
    """
    Итератор для обхода товаров в категории
    """
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
