from .component import Component

class Switch(Component):
    def __init__(self, name: str, price: float, switch_type: str):
        super().__init__(name, price)
        self.switch_type = switch_type

    @property
    def switch_type(self) -> str:
        return self._switch_type

    @switch_type.setter
    def switch_type(self, value: str):
        if not value:
            raise ValueError("Switch type must not be empty")
        self._switch_type = value

    def to_csv(self) -> list:
        return [self.name, self.price, self.switch_type]

    def display(self) -> str:
        return f"Switch: {self.name}, Price: ${self.price}, Type: {self.switch_type}"


