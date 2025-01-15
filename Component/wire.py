from component import Component

class Wire(Component):
    def __init__(self, name: str, price: float, length: float):
        super().__init__(name, price)
        self._length = length

    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._length = float(value)
        else:
            raise ValueError("Length must be a positive number")
        
    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Wire':
        name, price, length = csv_string.split(',')
        return cls(name, float(price), float(length)) 
    
    def duplicate(self) -> 'Wire':
        return Wire(self.name, self.price, self.length)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.length}"
    
    def display(self) -> str:
        return f"Wire: {self.name}, Price: ${self.price:.2f}, Length: {self.length}"