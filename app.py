import csv
from Component.battery import Battery
from Component.wire import Wire
from Component.solarpanel import SolarPanel
from Component.switch import Switch
from Component.sensor import Sensor
from Component.buzzer import Buzzer
from Light.LEDlight import LEDLight
from Light.lightglobe import LightGlobe


class App:
    def __init__(self):
        self.components = []
        self.filename = "components.csv"

    def load_data(self):
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "Battery":
                    self.components.append(Battery(row[1], float(row[2]), float(row[3]), int(row[4])))
                elif row[0] == "Wire":
                    self.components.append(Wire(row[1], float(row[2]), float(row[3]), int(row[4])))
                elif row[0] == "Solar Panel":
                    self.components.append(SolarPanel(row[1], float(row[2]), float(row[3]), float(row[4])))
                elif row[0] == "Switch":
                    self.components.append(Switch(row[1], float(row[2]), row[3]))
                elif row[0] == "Sensor":
                    self.components.append(Sensor(row[1], float(row[2]), row[3], float(row[4])))
                elif row[0] == "Buzzer":
                    self.components.append(Buzzer(row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6])))
                elif row[0] == "LEDLight":
                    self.components.append(LEDLight(row[1], float(row[2]), float(row[3]), float(row[4]), row[5]))
                elif row[0] == "LightGlobe":
                    self.components.append(LightGlobe(row[1], float(row[2]), float(row[3]), float(row[4]), row[5]))

    def save_data(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for component in self.components:
                writer.writerow([component.__class__.__name__] + component.to_csv())

    def display_components(self):
        print("\nCOMPONENT MENU")
        if not self.components:
            print("No components available.")
        else:
            i = 1
            for component in self.components:
                print(f"{i}. {component.display()}")
                i += 1

    def add_component(self):
        print("\nNEW COMPONENT MENU")
        print("1. WIRE")
        print("2. BATTERY")
        print("3. SOLAR PANEL")
        print("4. LIGHT GLOBE")
        print("5. LED LIGHT")
        print("6. SWITCH")
        print("7. SENSOR")
        print("8. BUZZER")
        print("9. BACK")
        choice = input("Please enter a number: ")

        if choice == "1":
            print("\nNEW WIRE")
            length = input("Please enter length (mm): ")
            price = input("Please enter price: ")
            number = input("Please enter number of Wires: ")
            self.components.append(Wire("Wire", float(price), float(length), int(number)))
            print(f"Added {length}mm Wire ${price} X {number}")

        elif choice == "2":
            print("\nNEW BATTERY")
            print("Battery sizes are AA or AAA or C or D or E")
            size = input("Please enter battery size: ")
            if size in ["AA", "AAA", "C"]:
                valid_voltages = [1.2, 1.5]
            elif size == "D":
                valid_voltages = [1.5]
            elif size == "E":
                valid_voltages = [9.0]
            else:
                print("Invalid battery size. Please try again.")
                return
            voltage = float(input("Please enter a voltage that matches the battery size: "))
            while voltage not in valid_voltages:
                print("Error, please enter the right voltage.")
                voltage = float(input("Please enter a voltage that matches the battery size: "))
            price = input("Please enter price: ")
            number = input("Please enter number of Batteries: ")
            self.components.append(Battery(size, float(price), voltage, int(number)))
            print(f"Added {voltage}V {size} Battery ${price} X {number}")

        elif choice == "3":
            print("\nNEW SOLAR PANEL")
            print("Voltage is usually between 1 and 12")
            voltage = input("Please enter voltage (V): ")
            print("Current is usually between 100 and 1000 milliAmps")
            current = input("Please enter current (mA): ")
            price = input("Please enter price: ")
            number = input("Please enter number of Solar Panels: ")
            self.components.append(SolarPanel("Solar Panel", float(price), float(voltage), float(current)))
            print(f"Added {voltage}V {current}mA Solar Panel ${price} X {number}")

        elif choice == "4":
            print("\nNEW LIGHT GLOBE")
            print("Light Globe Colours: warm, neutral, cool")
            colour = input("Please enter light globe colour: ")
            print("Voltage is usually between 1 and 12")
            voltage = input("Please enter voltage (V): ")
            print("Current is usually between 100 and 1000 milliAmps")
            current = input("Please enter current (mA): ")
            price = input("Please enter price: ")
            number = input("Please enter number of Light Globes: ")
            self.components.append(LightGlobe("Light Globe", float(price), float(voltage), float(current), colour))
            print(f"Added {voltage}V {current}mA {colour.capitalize()} Light Globe ${price} X {number}")

        elif choice == "5":
            print("\nNEW LED LIGHT")
            print("LED Light Colours: white, red, green, blue, yellow, orange, pink, aqua, violet")
            colour = input("Please enter LED light colour: ")
            print("Voltage is usually between 1 and 12")
            voltage = input("Please enter voltage (V): ")
            print("Current is usually between 100 and 1000 milliAmps")
            current = input("Please enter current (mA): ")
            price = input("Please enter price: ")
            number = input("Please enter number of LED Lights: ")
            self.components.append(LEDLight("LED Light", float(price), float(voltage), float(current), colour,))
            print(f"Added {voltage}V {current}mA {colour.capitalize()} LED Light ${price} X {number}")

        elif choice == "6":
            print("\nNEW SWITCH")
            print("Switch types: push, slide, rocker, toggle")
            switch_type = input("Please enter switch type: ")
            print("Voltage is usually between 1 and 12 ")
            price = input("Please enter price: ")
            number = input("Please enter number of Switches: ")
            self.components.append(Switch("Switch", float(price), switch_type))
            print(f"Added {switch_type.capitalize()} Switch ${price} X {number}")

        elif choice == "7":
            print("\nNEW SENSOR")
            print("Sensor types: light, motion, infrared, sound, touch, dust, temperature, humidity")
            sensor_type = input("Please enter sensor type: ")
            print("Voltage is usually between 1 and 12 ")
            voltage = input("Please enter voltage (V): ")
            price = input("Please enter price: ")
            number = input("Please enter number of Sensors: ")
            self.components.append(Sensor(sensor_type, float(price), float(voltage), int(number)))
            print(f"Added {voltage}V {sensor_type.capitalize()} Sensor ${price} X {number}")

        elif choice == "8":
            print("\nNEW BUZZER")
            frequency = input("Please enter frequency (Hz): ")
            sound_pressure = input("Please enter sound pressure (dB): ") 
            voltage = input("Please enter voltage (V): ")
            print("Current is usually between 100 and 1000 milliAmps")
            current = input("Please enter current (mA): ")
            price = input("Please enter price: ")
            number = input("Please enter number of Buzzers: ")
            self.components.append(Buzzer("Buzzer", float(price), float(frequency), float(sound_pressure), float(voltage), float(current)))
            print(f"Added {voltage}V {current}mA {frequency}Hz {sound_pressure}dB Buzzer ${price} X {number}")

        elif choice == "9":
            print("Returning to the previous menu.")
            return

        else:
            print("Invalid input. Please try again.")


    def component_menu(self):
        while True:
            print("\nCOMPONENT MENU")
            print("1. NEW COMPONENT")
            print("2. VIEW COMPONENTS")
            print("3. BACK")
            choice = input("Please enter a number: ")

            if choice == "1":
                self.add_component()
            elif choice == "2":
                self.display_components()
            elif choice == "3":
                break
            else:
                print("Wrong input, must be a number between 1 and 3.")
    def circuit_kits_menu(self):
        
    
        self.circuit_kits = [] 
        while True:
            print("\nCIRCUIT KITS MENU")
            print("1. CREATE CIRCUIT KIT")
            print("2. VIEW CIRCUIT KITS")
            print("3. BACK")
            choice = input("Please enter a number: ")

            if choice == "1":
                print("\nCREATE CIRCUIT KIT")
                kit_name = input("Please enter the name of the circuit kit: ")
                kit_components = []

                print("\nCOMPONENTS AVAILABLE:")
                for i in range(len(self.components)):
                    print(f"{i + 1}. {self.components[i].name}, Price: {self.components[i].price}")
                print(f"{len(self.components) + 1}. FINISH")

                while True:
                    component_choice = int(input("Select a component to add (or finish): "))
                    if component_choice == len(self.components) + 1:
                        break
                    kit_components.append(self.components[component_choice - 1])

                self.circuit_kits.append({"name": kit_name, "components": kit_components})

            elif choice == "2":
                print("\nVIEW CIRCUIT KITS")
                for i in range(len(self.circuit_kits)):
                    print(f"{i + 1}. Circuit Kit: {self.circuit_kits[i]['name']}")
                    print("   Components:")
                    for component in self.circuit_kits[i]['components']:
                        print(f"     - {component.name}, Price: {component.price}")

            elif choice == "3":
                break

            
    def run(self):
        self.load_data()
        while True:
            print("\nHOME MENU")
            print("1. COMPONENTS")
            print("2. CIRCUIT KITS")
            print("3. CLOSE")
            choice = input("Please enter a number: ")

            if choice == "1":
                self.component_menu()
            elif choice == "2":
                self.circuit_kits_menu()
            elif choice == "3":
                self.save_data()
                print("Data saved. Exiting.")
                break
            else:
                print("Wrong input, must be a number between 1 and 3.")

    


if __name__ == "__main__":
    app = App()
    app.run()