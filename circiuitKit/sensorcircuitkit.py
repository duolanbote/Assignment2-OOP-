from circuit import CircuitKit

class SensorCircuitKit(CircuitKit):
    

    def validate_circuit(self):
        
        return len(self.components) >= 2
