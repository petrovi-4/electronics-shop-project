from src.item import Item


class KeyboardLayoutMixin:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


class Keyboard(Item, KeyboardLayoutMixin):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        if language in ["EN", "RU"]:
            self.__language = language
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")