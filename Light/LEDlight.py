from .light import Light

class LEDLight(Light):
    def __init__(self, name: str, price: float, lumens: float, color: str):
        super().__init__(name, price, lumens)
        self.color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        if not value:
            raise ValueError("Color must not be empty")
        self._color = value

    def to_csv(self) -> list:
        return [self.name, self.price, self.lumens, self.color]

    def display(self) -> str:
        return f"LED Light: {self.name}, Price: ${self.price}, Lumens: {self.lumens}, Color: {self.color}"
