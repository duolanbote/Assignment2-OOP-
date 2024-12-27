menu1 = {
    "WIRE"
    "BATTERY"
    "SOLAR PANEL"
    "LIGHT GLOBE"
    "LED LIGHT"
    "SWITCH"
    "BUZZER"
    "BACK"
}

class Memu():
    def __init__(self, title, option):
        self._title = title
        self._option = option
        pass


    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, set_title):
        self._title = set_title
        pass


    @property
    def option(self):
        return self._option
    @option.setter
    def option(self, option_selection):
        self._option = option_selection
        pass

    @property
    def choice(self):
        return self._choice
    @choice.setter
    def choice(self, choiceselection):
        self._choice = int(choiceselection)
        pass

    def input(self):
        user_input = input("Please enter a number: ")
        self.choice = user_input
        return self.choice
        
    def menu():
        print('Home menu')
        print('1. COMPONENTS')
        print('2. CIRCUIT KITS')
        print('3. CLOSE')
        choice = input('Please enter a number')

        if choice == '1':
            menu1()
        elif choice == '2':
            menu2()
    




    
#12