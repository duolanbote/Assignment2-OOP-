from .component import Component

class Wire(Component):
    def __init__(self, name: str, price: float, length: float, number: int):
        super().__init__(name, price)
        self.length = length
        self.number = number

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float):
        if value <= 0:
            raise ValueError("Length must be a positive number")
        self._length = float(value)

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int):
        if value <= 0:
            raise ValueError("Number must be a positive integer")
        self._number = int(value)

    def to_csv(self) -> list:
        return [self.name, self.price, self.length, self.number]

    def display(self) -> str:
        return f"Wire: {self.name}, Price: ${self.price}, Length: {self.length}mm, Quantity: {self.number}"
