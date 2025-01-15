from .light import Light


class LEDLight(Light):
    def __init__(self, name: str, price: float, voltage: float, current: float, color: str):
        super().__init__(name, price)
        self.voltage = voltage
        self.current = current
        self.color = color

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        if float(value) <= 0:
            raise ValueError("Voltage must be positive.")
        self._voltage = float(value)

    @property
    def current(self) -> float:
        return self._current

    @current.setter
    def current(self, value: float):
        if value <= 0:
            raise ValueError("Current must be positive.")
        self._current = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        if not value:
            raise ValueError("Color must not be empty.")
        self._color = value

    def duplicate(self):
        return LEDLight(self.name, self.price, self.voltage, self.current, self.color)

    def to_csv(self) -> list:
        return [self.name, self.price, self.voltage, self.current, self.color]

    def display(self) -> str:
        return f"LED Light: {self.name}, Price: ${self.price}, Voltage: {self.voltage}V, Current: {self.current}mA, Color: {self.color}"

    @classmethod
    def parse_csv(cls, csv_string: str):
        name, price, voltage, current, color = csv_string.split(',')
        return cls(name, float(price), float(voltage), float(current), color)
