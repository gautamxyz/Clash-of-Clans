from colorama import Fore, Back, Style 

class Hut:
    def __init__ (self,x,y):
        self.height=1
        self.width=1
        x=5
        y=5
        self.health=3
        self.pixel3 = Back.MAGENTA+' H'+Style.RESET_ALL
        self.pixel2 = Back.BLUE+' H'+Style.RESET_ALL
        self.pixel1 = Back.WHITE+' H'+Style.RESET_ALL