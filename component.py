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

    def duplicate(self) -> 'SolarPanel':
        return SolarPanel(self.name, self.price, self.voltage, self.wattage)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.voltage},{self.wattage}"

    def display(self) -> str:
        return f"Solar Panel: {self.name}, Price: ${self.price:.2f}, Voltage: {self.voltage}, Wattage: {self.wattage}"

class Battery(PowerSupply):
    def __init__(self, name: str, price: float, voltage: float, capacity: float):
        super().__init__(name, price, voltage)
        self._capacity = capacity

    @property
    def capacity(self) -> float:
        return self._capacity
    
    @capacity.setter
    def capacity(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._capacity = float(value)
        else:
            raise ValueError("Capacity must be a positive number")

    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Battery':
        name, price, voltage, capacity = csv_string.split(',')
        return cls(name, float(price), float(voltage), float(capacity))

    def duplicate(self) -> 'Battery':
        return Battery(self.name, self.price, self.voltage, self.capacity)

    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.voltage},{self.capacity}"

    def display(self) -> str:
        return f"Battery: {self.name}, Price: ${self.price:.2f}, Voltage: {self.voltage}, Capacity: {self.capacity}"

class InputComponent(Component, ABC):
    pass

class Switch(InputComponent):
    def __init__(self, name: str, price: float, type: str):
        super().__init__(name, price)
        self._type = type

    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, value: str):
        if isinstance(value, str):
            self._type = value
        else:
            raise ValueError("Type must be a string")
        
    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Switch':
        name, price, type = csv_string.split(',')
        return cls(name, float(price), type)

    def duplicate(self) -> 'Switch':
        return Switch(self.name, self.price, self.type)
    
    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.type}"

    def display(self) -> str:
        return f"Switch: {self.name}, Price: ${self.price:.2f}, Type: {self.type}"
    
class Sensor(InputComponent):
    def __init__(self, name: str, price: float, measurement: str):
        super().__init__(name, price)
        self._measurement = measurement

    @property
    def measurement(self) -> str:
        return self._measurement

    @measurement.setter
    def measurement(self, value: str):
        if isinstance(value, str):
            self._measurement = value
        else:
            raise ValueError("Measurement must be a string")
        
    @classmethod
    def parse_csv(cls, csv_string: str) -> 'Sensor':
        name, price, measurement = csv_string.split(',')
        return cls(name, float(price), measurement)

    def duplicate(self) -> 'Sensor':
        return Sensor(self.name, self.price, self.measurement)
    
    def to_csv(self) -> str:
        return f"{self.name},{self.price},{self.measurement}"

    def display(self) -> str:
        return f"Sensor: {self.name}, Price: ${self.price:.2f}, Measurement: {self.measurement}"
    
class OutputComponent(Component, ABC):
    pass
                      