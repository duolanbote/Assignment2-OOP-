class Circuit:
    def __init__(self):
        self.components = [] 
    
    def parse_csv(self, csv_string):
        self.components = []
        lines = csv_string.strip().split('\n')
        for line in lines:
            attributes = line.split(',')
            component = Component(*attributes)
            self.components.append(component)

    def