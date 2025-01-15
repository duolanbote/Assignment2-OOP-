from .component import Component

class Sensor(Component):
    def __init__(self, name: str, price: float, measurement: str):
        super().__init__(name, price)
        self.measurement = measurement

    @property
    def measurement(self) -> str:
        return self._measurement

    @measurement.setter
    def measurement(self, value: str):
        self._measurement = value

    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Sensor':
        name, price, measurement = csv_string.split(',')
        return cls(name, float(price), measurement)

    def duplicate(self) -> 'Sensor':
        return Sensor(self.name, self.price, self.measurement)

    def to_csv(self) -> list:
        return [self.name, self.price, self.measurement]

    def display(self) -> str:
        return f"Sensor: {self.name}, Price: ${self.price:.2f}, Measurement: {self.measurement}"



