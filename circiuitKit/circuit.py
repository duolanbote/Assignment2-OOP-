class CircuitKit:

    def __init__(self, name):
        self._name = name
        self._components = []  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:  
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, list):  
            self._components = value
        else:
            raise ValueError("Components must be a list.")

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        if component in self._components:
            self._components.remove(component)

    def display(self):
        print("Circuit Name:", self._name)
        if not self._components:
            print("No components in the circuit.")
        else:
            print("Components:")
            for component in self._components:
                print(component)

    def validate_circuit(self):
        return len(self._components) > 0

