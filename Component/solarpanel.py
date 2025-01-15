from .component import Component

class SolarPanel(Component):
    def __init__(self, name: str, price: float, voltage: float, wattage: float):
        super().__init__(name, price)
        self.voltage = voltage
        self.wattage = wattage

    @property
    def wattage(self) -> float:
        return self._wattage
        
    @wattage.setter
    def wattage(self, value):
        try:
            value = float(value)  # 尝试将输入转换为浮点数
            if value > 0:
                self._wattage = value
            else:
                raise ValueError("wattage must be a positive number")
        except ValueError:
            raise ValueError("wattage must be a valid positive number")


    @classmethod
    def parse_csv(cls, csv_string: str) -> 'SolarPanel':
        name, price, voltage, wattage = csv_string.split(',')
        return cls(name, float(price), float(voltage), float(wattage))

    def duplicate(self) -> 'SolarPanel':
        return SolarPanel(self.name, self.price, self.voltage, self.wattage)

    def to_csv(self) -> str:
        return [self.name,self.price,self.voltage,self.wattage]

    def display(self) -> str:
        return f"Solar Panel: {self.name}, Price: ${self.price:.2f}, Voltage: {self.voltage}, Wattage: {self.wattage}"
