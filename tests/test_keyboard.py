import pytest

from src.keyboard import Keyboard


def test_initial_language():
    keyboard = Keyboard('Test Keyboard', 100, 10)
    assert keyboard.language == "EN"


def test_change_language():
    keyboard = Keyboard('Test Keyboard', 100, 10)
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"


def test_set_language():
    keyboard = Keyboard('Test Keyboard', 100, 10)
    keyboard.language = "RU"
    assert keyboard.language == "RU"


def test_invalid_language():
    keyboard = Keyboard('Test Keyboard', 100, 10)
    with pytest.raises(AttributeError):
        keyboard.language = "CH"
