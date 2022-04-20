from colorama import Fore, Back, Style 
from src.building import Building

class Townhall(Building):
    def __init__ (self,x,y):
        self.height=4
        self.width=3
        #self.x=x
        #self.y=y
        self.pixel5 = Back.MAGENTA+' T'+Style.RESET_ALL
        self.pixel4 = Back.LIGHTMAGENTA_EX+' T'+Style.RESET_ALL
        self.pixel3 = Back.BLUE+' T'+Style.RESET_ALL
        self.pixel2 = Back.LIGHTBLUE_EX+' T'+Style.RESET_ALL
        self.pixel1 = Back.WHITE+' T'+Style.RESET_ALL