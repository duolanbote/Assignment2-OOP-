from Component.component import Component


class Light(Component):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    def duplicate(self):
        return Light(self.name, self.price)

    def to_csv(self) -> list:
        return [self.name, self.price]

    def display(self) -> str:
        return f"Light: {self.name}, Price: ${self.price}"

    def calculate_energy_efficiency(self, power_consumption: float) -> float:
       
        return self.price / power_consumption

    def is_expensive(self, threshold: float) -> bool:
        
        return self.price > threshold
