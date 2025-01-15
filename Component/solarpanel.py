from component import Component

class SolarPanel(PowerSupply):
    def __init__(self, name: str, price: float, voltage: float, wattage: float):
        super().__init__(name, price, voltage)
        self._wattage = wattage

    @property
    def wattage(self) -> float:
        return self._wattage
    
    @wattage.setter
    def wattage(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._wattage = float(value)
        else:
            raise ValueError("Wattage must be a positive number")

    @classmethod
    def parse_csv(cls, csv_string: str) -> 'SolarPanel':
        name, price, voltage, wattage = csv_string.split(',')
        return cls(name, float(price), float(voltage), float(wattage))

    def duplicate(self) -> 'SolarPanel':
        return SolarPanel(self.name, self.price, self.voltage, self.wattage)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.voltage},{self.wattage}"

    def display(self) -> str:
        return f"Solar Panel: {self.name}, Price: ${self.price:.2f}, Voltage: {self.voltage}, Wattage: {self.wattage}"
