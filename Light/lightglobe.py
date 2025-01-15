from light import Light

class LightGlobe(Light):
    def __init__(self, name: str, price: float, lumens: float, wattage: float):
        super().__init__(name, price, lumens)
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
    def parse_csv(cls, csv_string: str) -> 'LightGlobe':
        name, price, lumens, wattage = csv_string.split(',')
        return cls(name, float(price), float(lumens), float(wattage))
    
    def duplicate(self) -> 'LightGlobe':
        return LightGlobe(self.name, self.price, self.lumens, self.wattage)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.lumens},{self.wattage}"

    def display(self) -> str:
        return f"Light Globe: {self.name}, Price: ${self.price:.2f}, Lumens: {self.lumens}, Wattage: {self.wattage}"