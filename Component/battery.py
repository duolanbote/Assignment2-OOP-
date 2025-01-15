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
            raise ValueError("Voltage must be a positive number")
        self._voltage = float(value)

    @property
    def capacity(self) -> float:
        return self._capacity

    @capacity.setter
    def capacity(self, value: float):
        if value <= 0:
            raise ValueError("Capacity must be a positive number")
        self._capacity = float(value)

    def to_csv(self) -> list:
        return [self.name, self.price, self.voltage, self.capacity]

    def display(self) -> str:
        return f"Battery: {self.name}, Price: ${self.price}, Voltage: {self.voltage}V, Capacity: {self.capacity}mAh"
