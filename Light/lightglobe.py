from .light import Light

class LightGlobe(Light):
    def __init__(self, name: str, price: float, lumens: float, wattage: float):
        super().__init__(name, price, lumens)
        self.wattage = wattage

    @property
    def wattage(self) -> float:
        return self._wattage

    @wattage.setter
    def wattage(self, value: float):
        if value <= 0:
            raise ValueError("Wattage must be a positive number")
        self._wattage = float(value)

    def to_csv(self) -> list:
        return [self.name, self.price, self.lumens, self.wattage]

    def display(self) -> str:
        return f"Light Globe: {self.name}, Price: ${self.price}, Lumens: {self.lumens}, Wattage: {self.wattage}W"
