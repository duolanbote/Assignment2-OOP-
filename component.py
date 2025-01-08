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