from .component import Component

class Battery(Component):
    def __init__(self, name: str, price: float, voltage: float, capacity: float):
        super().__init__(name, price)
        self.voltage = voltage
        self.capacity = capacity

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, value: float):
        if value <= 0:
            raise ValueError("Voltage must be positive.")
        self._voltage = value

    @property
    def capacity(self) -> float:
        return self._capacity

    @capacity.setter
    def capacity(self, value: float):
        if value <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity = value

    def calculate_runtime(self, load_current: float) -> float:
        return self.capacity / load_current

    def duplicate(self):
        return Battery(self.name, self.price, self.voltage, self.capacity)

    def to_csv(self) -> list:
        return [self.name, self.price, self.voltage, self.capacity]

    def display(self) -> str:
        return f"Battery: {self.name}, Price: ${self.price}, Voltage: {self.voltage}V, Capacity: {self.capacity}mAh"

    @classmethod
    def parse_csv(cls, csv_string: str):
        name, price, voltage, capacity = csv_string.split(',')
        return cls(name, float(price), float(voltage), float(capacity))
