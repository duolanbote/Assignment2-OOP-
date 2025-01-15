from .component import Component

class Wire(Component):
    def __init__(self, name: str, price: float, length: float, quantity: int):
        super().__init__(name, price)
        self.length = length
        self.quantity = quantity

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float):
        if value <= 0:
            raise ValueError("Length must be positive.")
        self._length = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value <= 0:
            raise ValueError("Quantity must be positive.")
        self._quantity = value

    def total_length(self) -> float:
        return self.length * self.quantity

    def duplicate(self):
        return Wire(self.name, self.price, self.length, self.quantity)

    def to_csv(self) -> list:
        return [self.name, self.price, self.length, self.quantity]

    def display(self) -> str:
        return f"Wire: {self.name}, Price: ${self.price}, Length: {self.length}mm, Quantity: {self.quantity}"

    @classmethod
    def parse_csv(cls, csv_string: str):
        name, price, length, quantity = csv_string.split(',')
        return cls(name, float(price), float(length), int(quantity))
