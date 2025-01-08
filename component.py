from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price