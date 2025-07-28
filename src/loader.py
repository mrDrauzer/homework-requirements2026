import json
from .models import Product, Category

def load_data_from_json(filename):
    """
    Загружает категории и товары из JSON-файла,
    создаёт объекты через classmethod и добавляет продукты через add_product().
    Если встречается товар с нулевым количеством, он пропускается с выводом предупреждения.
    """

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    # Определяем, где находится список категорий: в корне, или под ключом "categories"
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
            products=[]
        )
        for prod_data in cat_data.get("products", []):
            try:
                product = Product.new_product(prod_data)
            except ValueError as e:
                print(f"Пропущен товар '{prod_data.get('name', 'Неизвестный')}' в категории '{cat_data.get('name', 'Неизвестная')}': {e}")
                continue  # пропускаем товар с ошибкой
            category.add_product(product)

        categories.append(category)

    return categories
