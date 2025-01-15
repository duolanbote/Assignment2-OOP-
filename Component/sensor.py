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
        if not value:
            raise ValueError("Measurement type must not be empty")
        self._measurement = value

    def to_csv(self) -> list:
        return [self.name, self.price, self.measurement]

    def display(self) -> str:
        return f"Sensor: {self.name}, Price: ${self.price}, Measurement: {self.measurement}"
