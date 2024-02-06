from typing import List

import pytest

from src.config import ROOT_DIR
from src.item import Item


def test_add_item_to_item():
    item1 = Item('Смартфон', 5000, 10)
    item2 = Item('Кабель', 100, 20)
    result = item1 + item2
    assert result == 30


def test_add_phone_and_item_reverse():
    item = Item('Смартфон', 5000, 10)
    other_object = 'some_object'
    with pytest.raises(TypeError):
        result = item + other_object


@pytest.mark.parametrize(
    "name, price, quantity, expected_total_price", [
        ("Смартфон", 10000, 20, 200000),
    ]
)
def test_calculate_total_price(name, price, quantity, expected_total_price):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == expected_total_price


@pytest.mark.parametrize(
    "name, price, quantity, pay_rate, expected_price", [
        ("Смартфон", 10000, 20, 0.8, 8000.0),
    ]
)
def test_apply_discount(name, price, quantity, pay_rate, expected_price):
    item = Item(name, price, quantity)
    item.pay_rate = pay_rate
    item.apply_discount()
    assert item.price == expected_price


@pytest.mark.parametrize(
    ('items', 'expected_data'), [
        ([
             Item("Смартфон", 10000, 20),
             Item("Ноутбук", 20000, 5)
         ],
         [
             {'name': 'Смартфон', 'price': 10000.0, 'quantity': 20},
             {'name': 'Ноутбук', 'price': 20000.0, 'quantity': 5}
         ])
    ]
)
def test_all_items_list(items, expected_data):
    actual_data: List[dict] = [
        {'name': item.name, 'price': item.price, 'quantity': item.quantity
         } for item in items]
    assert actual_data == expected_data


@pytest.mark.parametrize(
    ('filename', 'expected_items'), [
        (ROOT_DIR / 'items.csv', [
            {'name': 'Смартфон', 'price': 100.0, 'quantity': 1},
            {'name': 'Ноутбук', 'price': 1000.0, 'quantity': 3},
            {'name': 'Кабель', 'price': 10.0, 'quantity': 5},
            {'name': 'Мышка', 'price': 50.0, 'quantity': 5},
            {'name': 'Клавиатура', 'price': 75.0, 'quantity': 5},
        ]),
    ]
)
def test_instantiate_from_csv(filename, expected_items):
    Item.instantiate_from_csv(filename)
    actual_items: List[Item] = Item.all
    actual_data: List[dict] = [
        {'name': item.name, 'price': item.price, 'quantity': item.quantity}
        for item in actual_items
    ]

    print('Fact_elem: ')
    print(actual_items)
    print('Expected_elem: ')
    print(expected_items)
    assert actual_data == expected_items


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_repr():
    item = Item('Смартфон', 10000.0, 5)
    assert repr(item) == "Item('Смартфон', 10000.0, 5)"


def test_item_str():
    item = Item('Смартфон', 10000.0, 5)
    assert str(item) == 'Смартфон'
