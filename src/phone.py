from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', {self.price}, "
                f"{self.quantity}, {self.__number_of_sim})")

    def __add__(self, other):
        if not isinstance(other, Item) and not isinstance(other, Phone):
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'{self.__class__.__name__}' and '{type(other).__name__}'"
            )
        result = self.quantity + other.quantity
        return result

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count: int):
        if isinstance(count, int) and count > 0:
            self.__number_of_sim = count
        else:
            raise ValueError(
                'Количество физических SIM-карт должно быть целым числом больше нуля.'
            )
