import csv
from src.config import ROOT_DIR


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}('{self.__name}', {self.price}, "
                f"{self.quantity})")

    def __str__(self) -> str:
        return self.__name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_amount = self.price * self.quantity
        return total_amount

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        cls.clear_all()

        filepath = ROOT_DIR / filename

        with open(filepath, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)


    @classmethod
    def clear_all(cls):
        cls.all = []

    @staticmethod
    def string_to_number(num_str: str) -> float:
        return int(float(num_str))


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    Item.instantiate_from_csv('items.csv')  # оставляем имя файла без изменений
    print("Actual items:")
    for item in Item.all:
        print(item.name, item.price, item.quantity)  # Выводим имена всех
        # элементов
        # для отладки
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    print("Assertion passed successfully.")
    print(repr(item1))
    print(str(item1))
