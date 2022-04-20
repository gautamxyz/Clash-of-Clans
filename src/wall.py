from colorama import Fore, Back, Style 

class Wall:
    def __init__ (self,x,y):
        self.height=1
        self.width=1
        x=5
        y=5
        self.pixel = Back.BLACK+' W'+Style.RESET_ALL