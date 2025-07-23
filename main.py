import json
from src.loader import load_data_from_json
from src.models import Product, Category

def main():
    print("=== Интернет-магазин ===")

    try:
        categories = load_data_from_json("basa/products.json")

        # Вывод информации о каждой категории и её товарах
        for category in categories:
            print(f"\nКатегория: {category.name}")
            print(f"Описание: {category.description}")
            print("Товары:")
            print(category.products)  # вызывается геттер products, возвращает строку

        # Статистика
        print("\nОбщая статистика:")
        print(f"Всего категорий: {Category.total_categories}")
        print(f"Всего товаров: {Category.total_products}")

    except FileNotFoundError:
        print("Ошибка: файл products.json не найден!")
    except json.JSONDecodeError:
        print("Ошибка: неверный формат JSON!")

if __name__ == "__main__":
    main()
