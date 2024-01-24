from typing import List
import pytest
from src.item import Item


@pytest.mark.parametrize("name, price, quantity, expected_total_price", [
	("Смартфон", 10000, 20, 200000),
])
def test_calculate_total_price(name, price, quantity, expected_total_price):
	item = Item(name, price, quantity)
	assert item.calculate_total_price() == expected_total_price


@pytest.mark.parametrize("name, price, quantity, pay_rate, expected_price", [
	("Смартфон", 10000, 20, 0.8, 8000.0),
])
def test_apply_discount(name, price, quantity, pay_rate, expected_price):
	item = Item(name, price, quantity)
	item.pay_rate = pay_rate
	item.apply_discount()
	assert item.price == expected_price


@pytest.mark.parametrize(('items', 'expected_data'), [
	([
		 Item("Смартфон", 10000, 20),
		 Item("Ноутбук", 20000, 5)
	 ],
	 [
		 {'name': 'Смартфон', 'price': 10000.0, 'quantity': 20},
		 {'name': 'Ноутбук', 'price': 20000.0, 'quantity': 5}
	 ])
])
def test_all_items_list(items, expected_data):
	actual_data: List[dict] = [
		{'name': item.name, 'price': item.price, 'quantity': item.quantity
		 } for item in items]
	assert actual_data == expected_data
