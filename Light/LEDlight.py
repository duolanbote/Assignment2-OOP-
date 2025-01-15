from light import Light


class LEDLight(Light):
    def __init__(self, name: str, price: float, lumens: float, color: str):
        super().__init__(name, price, lumens)
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError("Color must be a string")
        
    @classmethod
    def parse_csv(cls, csv_string: str) -> 'LEDLight':
        name, price, lumens, color = csv_string.split(',')
        return cls(name, float(price), float(lumens), color)

    def duplicate(self) -> 'LEDLight':
        return LEDLight(self.name, self.price, self.lumens, self.color)
    
    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.lumens},{self.color}"

    def display(self) -> str:
        return f"LED Light: {self.name}, Price: ${self.price:.2f}, Lumens: {self.lumens}, Color: {self.color}"