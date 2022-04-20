from colorama import Fore, Back, Style
from matplotlib.pyplot import cla 
from src.headerss import cannons
from src.headerss import wizard_towers
from src.building import Building
from src.headerss import wizard_towers
class Cannon(Building):
    def __init__ (self,r,n,x,y):
        super().__init__(x,y,r,height=1,width=1,health=2,n=n)
        #self.height=1
        #self.width=1
        #self.range=7
        #self.damage_val=n
        #self.x=x
        #self.y=y
        #self.health=2
        self.pixel2 = Back.YELLOW+' C'+Style.RESET_ALL
        self.pixel1 = Back.WHITE+' C'+Style.RESET_ALL
        cannons.append([x,y,self.health])

class Wizard_Tower(Building):
    def __init__(self, r, n,x,y):
        """
        Initialize the TownHall class.
        """
        super().__init__(x,y,r,height=1,width=1,health=2,n=n)

        # Call the parent class' constructor
        #super().__init__(r, n,x,y)

        # Set the building's ASCII art and color
        self.pixel2 = Back.YELLOW+' W'+Style.RESET_ALL
        self.pixel1 = Back.WHITE+' W'+Style.RESET_ALL
        wizard_towers.append([x,y,self.health])
        #self.color = Fore.WHITE