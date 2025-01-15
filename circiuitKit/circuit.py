class CircuitKit:
    def __init__(self, name: str):
        self._name = name
        self._components = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def components(self) -> list:
        return self._components

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        if component in self._components:
            self._components.remove(component)

    def check_power_supply(self) -> bool:
        for component in self._components:
            if component.__class__.__name__ in ["Battery", "SolarPanel"]:
                return True
        return False

    def display(self) -> None:
        print(f"Circuit Name: {self._name}")
        if not self._components:
            print("No components in the circuit.")
        else:
            print("Components:")
            for component in self._components:
                print(component.display())



