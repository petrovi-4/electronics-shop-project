from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', {self.price}, "
                f"{self.quantity}, {self.number_of_sim})")

    def __add__(self, other):
        if not isinstance(other, Item) and not isinstance(other, Phone):
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'{self.__class__.__name__}' and '{type(other).__name__}'"
            )
        result = self.quantity + other.quantity
        return result
