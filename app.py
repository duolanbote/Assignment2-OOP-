import csv
from menu import Menu
from Component.battery import Battery
from Component.wire import Wire
from Component.solarpanel import SolarPanel
from Component.switch import Switch
from Component.sensor import Sensor
from Component.buzzer import Buzzer


class App:
    def __init__(self):
        self.components = []  # 用于存储所有组件
        self.filename = "data/components.csv"  # 数据文件路径

    def load_data(self):
        """
        从文件加载组件数据。
        """
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    component_type = row[0]
                    if component_type == "Battery":
                        self.components.append(Battery.parse_csv(",".join(row[1:])))
                    elif component_type == "Wire":
                        self.components.append(Wire.parse_csv(",".join(row[1:])))
                    elif component_type == "Solar Panel":
                        self.components.append(SolarPanel.parse_csv(",".join(row[1:])))
                    elif component_type == "Switch":
                        self.components.append(Switch.parse_csv(",".join(row[1:])))
                    elif component_type == "Sensor":
                        self.components.append(Sensor.parse_csv(",".join(row[1:])))
                    elif component_type == "Buzzer":
                        self.components.append(Buzzer.parse_csv(",".join(row[1:])))
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty list.")

    def save_data(self):
        """
        保存组件数据到文件。
        """
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                for component in self.components:
                    writer.writerow([type(component).__name__] + component.to_csv().split(","))
        except Exception as e:
            print(f"Error saving data: {e}")

    def display_components(self):
        """
        显示所有组件。
        """
        if not self.components:
            print("No components available.")
        else:
            for i, component in enumerate(self.components, start=1):
                print(f"{i}. {component.display()}")

    def add_component(self):
        """
        添加新组件。
        """
        print("\nAdd a Component")
        print("1. Battery")
        print("2. Wire")
        print("3. Solar Panel")
        print("4. Switch")
        print("5. Sensor")
        print("6. Buzzer")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter battery name: ")
            price = float(input("Enter battery price: "))
            voltage = float(input("Enter battery voltage: "))
            capacity = float(input("Enter battery capacity: "))
            self.components.append(Battery(name, price, voltage, capacity))
        elif choice == "2":
            name = input("Enter wire name: ")
            price = float(input("Enter wire price: "))
            length = float(input("Enter wire length: "))
            self.components.append(Wire(name, price, length))
        elif choice == "3":
            name = input("Enter solar panel name: ")
            price = float(input("Enter solar panel price: "))
            voltage = float(input("Enter solar panel voltage: "))
            wattage = float(input("Enter solar panel wattage: "))
            self.components.append(SolarPanel(name, price, voltage, wattage))
        elif choice == "4":
            name = input("Enter switch name: ")
            price = float(input("Enter switch price: "))
            switch_type = input("Enter switch type: ")
            self.components.append(Switch(name, price, switch_type))
        elif choice == "5":
            name = input("Enter sensor name: ")
            price = float(input("Enter sensor price: "))
            measurement = input("Enter sensor measurement: ")
            self.components.append(Sensor(name, price, measurement))
        elif choice == "6":
            name = input("Enter buzzer name: ")
            price = float(input("Enter buzzer price: "))
            volume = float(input("Enter buzzer volume: "))
            self.components.append(Buzzer(name, price, volume))
        else:
            print("Invalid choice. Returning to the menu.")

    def manage_menu(self):
        """
        主菜单逻辑。
        """
        while True:
            print("\nMain Menu")
            print("1. Display Components")
            print("2. Add Component")
            print("3. Save and Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_components()
            elif choice == "2":
                self.add_component()
            elif choice == "3":
                self.save_data()
                print("Exiting program. Data saved.")
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        """
        启动程序。
        """
        self.load_data()
        self.manage_menu()


if __name__ == "__main__":
    app = App()
    app.run()

