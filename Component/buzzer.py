from .component import Component
class Buzzer(Component):
    def __init__(self, name: str, price: float, volume: float):
        super().__init__(name, price)
        self.volume = volume

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float):
        if value <= 0:
            raise ValueError("Volume must be positive.")
        self._volume = value

    def calculate_sound_level(self, distance: float) -> float:
        return self.volume / (distance**2) if distance > 0 else 0

    def duplicate(self):
        return Buzzer(self.name, self.price, self.volume)

    def to_csv(self) -> list:
        return [self.name, self.price, self.volume]

    def display(self) -> str:
        return f"Buzzer: {self.name}, Price: ${self.price}, Volume: {self.volume}dB"

    @classmethod
    def parse_csv(cls, csv_string: str):
        name, price, volume = csv_string.split(',')
        return cls(name, float(price), float(volume))
