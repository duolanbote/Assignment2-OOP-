from .component import Component

class Wire(Component):
    def __init__(self, name: str, price: float, length: float):
        super().__init__(name, float(price))
        self.length = length

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float):
        if value > 0:
            self._length = value
        else:
            raise ValueError("Length must be a positive number")

    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Wire':
        name, price, length = csv_string.split(',')
        return cls(name, float(price), float(length))

    def duplicate(self) -> 'Wire':
        return Wire(self.name, self.price, self.length)

    def to_csv(self) -> list:
        return [self.name, self.price, self.length]

    def display(self) -> str:
        return f"Wire: {self.name}, Price: ${self.price}, Length: {self.length}"
