import json
from .models import Product, Category

def load_data_from_json(filename):
    """
    Загружает категории и товары из JSON-файла,
    создаёт объекты через classmethod и добавляет продукты через add_product().
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    if isinstance(data, list):
        categories_data = data
    elif isinstance(data, dict) and "categories" in data:
        categories_data = data["categories"]
    else:
        raise ValueError("Неправильная структура JSON-файла")

    for cat_data in categories_data:
        category = Category(
            name=cat_data["name"],
            description=cat_data["description"],
            products=[]  # пустой список — в конструкторе
        )

        for prod_data in cat_data["products"]:
            product = Product.new_product(prod_data)
            category.add_product(product)

        categories.append(category)

    return categories
