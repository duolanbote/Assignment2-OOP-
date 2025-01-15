from .component import Component

class SolarPanel(Component):
    def __init__(self, name: str, price: float, voltage: float, wattage: float):
        super().__init__(name, price)
        self.voltage = voltage
        self.wattage = wattage

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, value: float):
        if value <= 0:
            raise ValueError("Voltage must be positive.")
        self._voltage = value

    @property
    def wattage(self) -> float:
        return self._wattage

    @wattage.setter
    def wattage(self, value: float):
        if value <= 0:
            raise ValueError("Wattage must be positive.")
        self._wattage = value

    def calculate_energy_output(self, hours: float) -> float:
        return self.wattage * hours

    def duplicate(self):
        return SolarPanel(self.name, self.price, self.voltage, self.wattage)

    def to_csv(self) -> list:
        return [self.name, self.price, self.voltage, self.wattage]

    def display(self) -> str:
        return f"Solar Panel: {self.name}, Price: ${self.price}, Voltage: {self.voltage}V, Wattage: {self.wattage}W"

    @classmethod
    def parse_csv(cls, csv_string: str):
        name, price, voltage, wattage = csv_string.split(',')
        return cls(name, float(price), float(voltage), float(wattage))
