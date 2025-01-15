from .component import Component

class Battery(Component):
    def __init__(self, name: str, price: float, voltage: float, capacity: float):
        super().__init__(name, price, voltage)
        self._capacity = capacity

    @property
    def capacity(self) -> float:
        return self._capacity
    
    @capacity.setter
    def capacity(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._capacity = float(value)
        else:
            raise ValueError("Capacity must be a positive number")

    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Battery':
        name, price, voltage, capacity = csv_string.split(',')
        return cls(name, float(price), float(voltage), float(capacity))

    def duplicate(self) -> 'Battery':
        return Battery(self.name, self.price, self.voltage, self.capacity)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.voltage},{self.capacity}"

    def display(self) -> str:
        return f"Battery: {self.name}, Price: ${self.price:.2f}, Voltage: {self.voltage}, Capacity: {self.capacity}"