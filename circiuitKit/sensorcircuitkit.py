from .circuit import CircuitKit

class SensorCircuitKit(CircuitKit):
    def __init__(self, name: str):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        if component in self.components:
            self.components.remove(component)

    def display_sensors(self):
        print(f"Sensors in '{self.name}':")
        found_sensors = False
        for component in self.components:
            if component.__class__.__name__ == "Sensor":
                print(component.display())
                found_sensors = True
        if not found_sensors:
            print("No sensors in the circuit.")

    def check_functioning(self):
        has_sensor = False
        has_power = False
        for component in self.components:
            if component.__class__.__name__ == "Sensor":
                has_sensor = True
            if component.__class__.__name__ in ["Battery", "SolarPanel"]:
                has_power = True
        return has_sensor and has_power
