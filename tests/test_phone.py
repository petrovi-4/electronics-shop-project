import pytest
from src.phone import Phone
from src.item import Item


def test_add_phone_and_item():
    phone = Phone('iPhone', 10000, 5, 2)
    item = Item('Смартфон', 5000, 10)
    result = phone + item
    assert result == 15


def test_add_two_phones():
    phone1 = Phone('iPhone', 100000, 5, 2)
    phone2 = Phone('Samsung', 50000, 3, 1)
    result = phone1 + phone2
    assert result == 8


def test_add_phone_and_invalid_object():
    phone = Phone('iPhone', 10000, 5, 2)
    other_object = 'some_object'
    with pytest.raises(TypeError):
        result = phone + other_object
