import csv
from Component.battery import Battery
from Component.wire import Wire
from Component.solarpanel import SolarPanel
from Component.switch import Switch
from Component.sensor import Sensor
from Component.buzzer import Buzzer




class App:
    def __init__(self):
        self.components = []  
        self.filename = "components.csv"  

    def load_data(self):
        
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == "Battery":
                        self.components.append(Battery(*row[1:]))
                    elif row[0] == "Wire":
                        self.components.append(Wire(*row[1:]))
                    elif row[0] == "Solar Panel":
                        self.components.append(SolarPanel(*row[1:]))
                    elif row[0] == "Switch":
                        self.components.append(Switch(*row[1:]))
                    elif row[0] == "Sensor":
                        self.components.append(Sensor(*row[1:]))
                    elif row[0] == "Buzzer":
                        self.components.append(Buzzer(*row[1:]))
        except FileNotFoundError:
            print("File not found")

    def save_data(self):
        
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for component in self.components:
                writer.writerow([component.name] + component.to_csv())


    def display_components(self):
        i = 1
        if not self.components:
            print("No components available.")
        else:
              
            for component in self.components:
                print(f"{i}. {component.display()}")
                i += 1  

    def add_component(self):
        
        print("1. Battery")
        print("2. Wire")
        print("3. Solar Panel")
        print("4. Switch")
        print("5. Sensor")
        print("6. Buzzer")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            price = input("Enter price: ")
            voltage = input("Enter voltage: ")
            capacity = input("Enter capacity: ")
            self.components.append(Battery(name, price, voltage, capacity))
        elif choice == "2":
            name = input("Enter name: ")
            price = input("Enter price: ")
            length = input("Enter length: ")
            self.components.append(Wire(name, price, length))
        elif choice == "3":
            name = input("Enter name: ")
            price = input("Enter price: ")
            voltage = input("Enter voltage: ")
            wattage = input("Enter wattage: ")
            self.components.append(SolarPanel(name, price, voltage, wattage))
        elif choice == "4":
            name = input("Enter name: ")
            price = input("Enter price: ")
            switch_type = input("Enter type: ")
            self.components.append(Switch(name, price, switch_type))
        elif choice == "5":
            name = input("Enter name: ")
            price = input("Enter price: ")
            measurement = input("Enter measurement: ")
            self.components.append(Sensor(name, price, measurement))
        elif choice == "6":
            name = input("Enter name: ")
            price = input("Enter price: ")
            volume = input("Enter volume: ")
            self.components.append(Buzzer(name, price, volume))
        else:
            print("Invalid choice.")

    def run(self):
        
        self.load_data()

        while True:
            print("\n1. Display Components")
            print("2. Add Component")
            print("3. Save and Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_components()
            elif choice == "2":
                self.add_component()
            elif choice == "3":
                self.save_data()
                print("Data saved. Exiting.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = App()
    app.run()


