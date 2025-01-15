from .component import Component

class SolarPanel(Component):
    def __init__(self, name: str, price: float, voltage: float, current: float):
        super().__init__(name, price)
        self.voltage = voltage
        self.current = current

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, value: float):
        if value <= 0:
            raise ValueError("Voltage must be a positive number")
        self._voltage = float(value)

    @property
    def current(self) -> float:
        return self._current

    @current.setter
    def current(self, value: float):
        if value <= 0:
            raise ValueError("Current must be a positive number")
        self._current = float(value)

    def to_csv(self) -> list:
        return [self.name, self.price, self.voltage, self.current]

    def display(self) -> str:
        return f"Solar Panel: {self.name}, Price: ${self.price}, Voltage: {self.voltage}V, Current: {self.current}mA"
