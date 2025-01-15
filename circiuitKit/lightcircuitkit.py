from .circuit import CircuitKit

class LightCircuitKit(CircuitKit):
    def __init__(self, name: str):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        if component in self.components:
            self.components.remove(component)

    def display_lights(self):
        print(f"Lights in '{self.name}':")
        found_lights = False
        for component in self.components:
            if component.__class__.__name__ in ["LightGlobe", "LEDLight"]:
                print(component.display())
                found_lights = True
        if not found_lights:
            print("No lights in the circuit.")

    def check_functioning(self):
        has_light = False
        has_power = False
        for component in self.components:
            if component.__class__.__name__ in ["LightGlobe", "LEDLight"]:
                has_light = True
            if component.__class__.__name__ in ["Battery", "SolarPanel"]:
                has_power = True
        return has_light and has_power

