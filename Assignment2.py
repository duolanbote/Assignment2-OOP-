class Menu:
    def __init__(self, title, options):
        self._title = title
        self._options = options
        self._choice = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        self._choice = value

    def display(self):
        
        print(f"\n{self._title}")
        print("-" * len(self._title))
        count = 1
        for option in self._options:
            print(f"{count}. {option}")
            count += 1
        print("0. Exit")

    def get_choice(self):
        try:
            user_input = int(input("Please enter a number: "))
            if 0 <= user_input <= len(self._options):
                self.choice = user_input
                return self.choice
            else:
                print("Invalid choice. Please try again.")
                return -1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return -1

    def run_once(self):
        self.display()
        choice = self.get_choice()

        if choice == 0:
            print("Exiting menu...")
            return False
        elif choice == 1:
            print("Manage Components")
        elif choice == 2:
            print("Manage Circuits")
        elif choice == 3:
            print("Close")
        else:
            print("Invalid choice. Please try again.")
        return True
