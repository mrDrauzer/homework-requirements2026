import json
from .models import Product, Category


def load_data_from_json(filename):
    """
    Загружает  категории и товары из JSON-файла.
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    # Если data - это список категорий
    if isinstance(data, list):
        categories_data = data
    # Если data - это словарь с ключом 'categories'
    elif isinstance(data, dict) and "categories" in data:
        categories_data = data["categories"]
    else:
        raise ValueError("Неправильная структура JSON-файла")

    for cat_data in categories_data:
        products = []
        for prod_data in cat_data["products"]:
            product = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                quantity=prod_data["quantity"],
            )
            products.append(product)

        category = Category(
            name=cat_data["name"],
            description=cat_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
