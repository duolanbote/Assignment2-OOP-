from component import Component

class Buzzer(Component):
    def __init__(self, name: str, price: float, volume: float):
        super().__init__(name, price)
        self._volume = volume

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._volume = float(value)
        else:
            raise ValueError("Volume must be a positive number")
        
    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Buzzer':
        name, price, volume = csv_string.split(',')
        return cls(name, float(price), float(volume))

    def duplicate(self) -> 'Buzzer':
        return Buzzer(self.name, self.price, self.volume)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.volume}"

    def display(self) -> str:
        return f"Buzzer: {self.name}, Price: ${self.price:.2f}, Volume: {self.volume}"