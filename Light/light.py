class Light():
    def __init__(self, name: str, price: float, lumens: float):
        super().__init__(name, price)
        self._lumens = lumens

    @property
    def lumens(self) -> float:
        return self._lumens

    @lumens.setter
    def lumens(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._lumens = float(value)
        else:
            raise ValueError("Lumens must be a positive number")