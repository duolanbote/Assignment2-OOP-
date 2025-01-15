from circuit import CircuitKit

class LightCircuitKit(CircuitKit):
    

    def validate_circuit(self):
        
        return len(self.components) >= 2
