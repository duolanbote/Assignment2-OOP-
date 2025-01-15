from component import Component

class Switch(Component):
    def __init__(self, name: str, price: float, type: str):
        super().__init__(name, price)
        self._type = type

    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, value: str):
        if isinstance(value, str):
            self._type = value
        else:
            raise ValueError("Type must be a string")
        
    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Switch':
        name, price, type = csv_string.split(',')
        return cls(name, float(price), type)

    def duplicate(self) -> 'Switch':
        return Switch(self.name, self.price, self.type)
    
    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.type}"

    def display(self) -> str:
        return f"Switch: {self.name}, Price: ${self.price:.2f}, Type: {self.type}"