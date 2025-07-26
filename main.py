import json
from src.loader import load_data_from_json
from src.models import Category


def main():
    print("=== Интернет-магазин ===")
    try:
        categories = load_data_from_json("basa/products.json")

        for category in categories:
            print(f"\nКатегория: {category.name}")
            print(f"Описание: {category.description}")
            print("Товары:")
            for product in category.products:
                print(product)

        print("\nОбщая статистика:")
        print(f"Всего категорий: {Category.category_count}")
        print(f"Всего товаров: {Category.product_count}")

    except FileNotFoundError:
        print("Ошибка: файл products.json не найден!")
    except json.JSONDecodeError:
        print("Ошибка: неверный формат JSON!")


if __name__ == "__main__":
    main()
