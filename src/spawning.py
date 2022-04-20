from colorama import Fore, Back, Style 

class Spawning():
    def __init__ (self,x,y):
        self.height=1
        self.width=1
        x=0
        y=0
        self.pixel = Back.LIGHTCYAN_EX+Fore.BLACK+' S'+Style.RESET_ALL