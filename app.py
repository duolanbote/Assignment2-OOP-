class App:
    def __init__(self):
        self.components = []
        self.circuit_kits = []

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.manage_components()
            elif choice == '2':