from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")
        
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = float(value)
        else:
            raise ValueError("Price must be a non-negative number")
        
    @classmethod
    @abstractmethod
    def parse_csv(cls, csv_string: str) -> 'Component':
        pass

    @abstractmethod
    def duplicate(self) -> 'Component':
        pass

    @abstractmethod
    def to_csv(self) -> str:
        pass

    @abstractmethod
    def display(self) -> str:
        pass

class Wire(Component):
    def __init__(self, name: str, price: float, length: float):
        super().__init__(name, price)
        self._length = length

    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._length = float(value)
        else:
            raise ValueError("Length must be a positive number")
        
    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Wire':
        name, price, length = csv_string.split(',')
        return cls(name, float(price), float(length)) 
    
    def duplicate(self) -> 'Wire':
        return Wire(self.name, self.price, self.length)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.length}"
    
    def display(self) -> str:
        return f"Wire: {self.name}, Price: ${self.price:.2f}, Length: {self.length}"
    
class PowerSupply(Component, ABC):
    def __init__(self, name: str, price: float, voltage: float):
        super().__init__(name, price)
        self._voltage = voltage

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._voltage = float(value)
        else:
            raise ValueError("Voltage must be a positive number")

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