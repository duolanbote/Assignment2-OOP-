class App:
    def __init__(self, value):
        self._value = value

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, list):
            self._components = value
        else:
            raise ValueError("Components must be a list")
    @property
    def circuit_kits(self):
        return self._circuit_kits

    @circuit_kits.setter
    def circuit_kits(self, value):
        if isinstance(value, list):
            self._circuit_kits = value
        else:
            raise ValueError("Circuit kits must be a list")