import json
from src.loader import load_data_from_json
from src.models import Product, Category


def main():
    """Основная функция программы"""
    print("=== Интернет-магазин === ")

    # Загрузка данных из JSON
    try:
        categories = load_data_from_json("basa/products.json")

        # Вывод информации о категориях и товарах
        for category in categories:
            print(f"\nКатегория: {category.name}")
            print(f"Описание: {category.description}")
            print("Товары:")

            for product in category.products:
                print(
                    f"  - {product.name}: {product.price} руб. "
                    f"(в наличии: {product.quantity})"
                )

        # Статистика
        print("\nОбщая статистика:")
        print(f"Всего категорий: {Category.total_categories}")
        total_products_count = sum(category.total_products for category in categories)
        print(f"Всего товаров: {total_products_count}")

    except FileNotFoundError:
        print("Ошибка: файл products.json не найден!")
    except json.JSONDecodeError:
        print("Ошибка: неверный формат JSON!")


if __name__ == "__main__":
    main()
