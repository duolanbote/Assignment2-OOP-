from .component import Component

class Buzzer(Component):
    def __init__(self, name: str, price: float, frequency: float, sound_pressure: float, voltage: float, current: float):
        super().__init__(name, price)
        self.frequency = frequency
        self.sound_pressure = sound_pressure
        self.voltage = voltage
        self.current = current

    @property
    def frequency(self) -> float:
        return self._frequency

    @frequency.setter
    def frequency(self, value: float):
        if value <= 0:
            raise ValueError("Frequency must be a positive number")
        self._frequency = float(value)

    @property
    def sound_pressure(self) -> float:
        return self._sound_pressure

    @sound_pressure.setter
    def sound_pressure(self, value: float):
        if value <= 0:
            raise ValueError("Sound pressure must be a positive number")
        self._sound_pressure = float(value)

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, value: float):
        if value <= 0:
            raise ValueError("Voltage must be a positive number")
        self._voltage = float(value)

    @property
    def current(self) -> float:
        return self._current

    @current.setter
    def current(self, value: float):
        if value <= 0:
            raise ValueError("Current must be a positive number")
        self._current = float(value)

    def to_csv(self) -> list:
        return [self.name, self.price, self.frequency, self.sound_pressure, self.voltage, self.current]

    def display(self) -> str:
        return f"Buzzer: {self.name}, Price: ${self.price}, Frequency: {self.frequency}Hz, Sound Pressure: {self.sound_pressure}dB, Voltage: {self.voltage}V, Current: {self.current}mA"
