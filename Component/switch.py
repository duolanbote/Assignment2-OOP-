from .component import Component

class Switch(Component):
    def __init__(self, name: str, price: float, switch_type: str):
        super().__init__(name, float(price))
        self.type = switch_type

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Switch':
        name, price, switch_type = csv_string.split(',')
        return cls(name, float(price), switch_type)

    def duplicate(self) -> 'Switch':
        return Switch(self.name, self.price, self.type)

    def to_csv(self) -> list:
        return [self.name, self.price, self.type]

    def display(self) -> str:
        return f"Switch: {self.name}, Price: ${self.price}, Type: {self.type}"
