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
    def __init__(self, option):
        self.option = option
        pass
    
    def getmenu(self):
        num = 1
        for i in range(len(self.option)):
            print(num + '.' + self.option)
            num += 1
            pass
    def menuselection(self):
        select = int(input('Please enter a number:'))
        if select < 1 or select > 3:
            print('Wrong input, must be a number between 1 and 3')
            select = int(input('Please enter a number:'))
        else:
            print()

#123