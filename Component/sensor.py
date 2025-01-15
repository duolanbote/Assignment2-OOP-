from .component import Component

class Sensor(Component):
    def __init__(self, name: str, price: float, measurement_type: str):
        super().__init__(name, price)
        self.measurement_type = measurement_type

    @property
    def measurement_type(self) -> str:
        return self._measurement_type

    @measurement_type.setter
    def measurement_type(self, value: str):
        if not value:
            raise ValueError("Measurement type cannot be empty.")
        self._measurement_type = value

    def detect(self, input_value) -> bool:
        return True if input_value else False

    def duplicate(self):
        return Sensor(self.name, self.price, self.measurement_type)

    def to_csv(self) -> list:
        return [self.name, self.price, self.measurement_type]

    def display(self) -> str:
        return f"Sensor: {self.name}, Price: ${self.price}, Measurement: {self.measurement_type}"

    @classmethod
    def parse_csv(cls, csv_string: str):
        name, price, measurement_type = csv_string.split(',')
        return cls(name, float(price), measurement_type)
