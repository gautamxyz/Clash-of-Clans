import imp
from time import sleep
import time
import threading
from pymysql import NULL
from src.archer import Archer
from src.headerss import throbricks
from src.input import get_input
from colorama import Fore, Back, Style
import random
from src.pattern import Pattern, bricks, spawns
from src.headerss import huts
from src.headerss import th
from src.barbarian import Barbarian
from src.balloon import Balloon
#from src.board import Board
from src.headerss import barbs,cannons,wizard_towers,archers
#from src.headerss import max_barb,curr_barb
from src.headerss import max_barb,curr_barb,xx,max_balloon,curr_balloon,balloons,max_archer,curr_archer,level
NUM_ROWS = 31
NUM_COLS = 80


class King():
    def set_xx(self,val):
        global xx
        xx=val

    def set_curr_barb(self):
        global curr_barb,curr_balloon,curr_archer
        curr_barb=0
        curr_balloon=0
        curr_archer=0
        self.damage=0

    def __init__(self, x, y):
        global xx
        self.x = x
        self.y = y

        #self.initial_width = 30

        self.height = 1
        self.width = 1
        self.health=10
        
        self.damage=1
        if xx==2:
            self.damage=self.damage/2
        self.last=NULL
        self.pixel=Back.RED+' K'+Style.RESET_ALL
        
        if xx==2:
            self.pixel = Back.RED+' Q'+Style.RESET_ALL
        
        self.bullet_launcher_pixel = Back.MAGENTA+' '+Style.RESET_ALL

    def update_position(self, x, y):
        self.x = x
        self.y = y
    def delayed_detection(self,char):
        time.sleep(1)
        self.queen_attack(char)
    def queen_attack(self,char):
        global xx
        #print(self.damage)
        #sleep(1)
        if self.last==NULL:
            return
        rangee=0
        aoe=0
        if char==' ':
            rangee=8
            aoe=2
        elif char=='e':
            rangee=16
            aoe=4
            
        
        if self.last=='d':
            x0=self.x+rangee
            y0=self.y
        elif self.last=='s':
            x0=self.x
            y0=self.y+rangee
        elif self.last=='a':
            x0=self.x-rangee
            y0=self.y
        elif self.last=='w':
            x0=self.x
            y0=self.y-rangee
        buf=[]
        s=0
        for i in range(x0-aoe,x0+aoe+1):
            for j in range(y0-aoe,y0+aoe+1):
                
                if i>=0 and j>=0 and i<NUM_COLS and j<NUM_ROWS:
                    for k in range(0, len(bricks)):
                        
                        if bricks[k][1] == i and bricks[k][0] == j:
                            throbricks.append((bricks[k][0], bricks[k][1]))
                        
                    for k in range(0,len(huts)):
                        x1=huts[k][1]
                        y1=huts[k][0]
                        fg=list(huts[k])
                        if(x1==i and y1==j):
                            
                            #print("theek")
                            
                            fg[2]-=self.damage
                            #huts[k]=tuple(fg)
                        if fg[2]>0:
                            buf.append(tuple(fg))
                    if(len(buf)>0):
                        huts.clear()
                    for m in range(0, len(buf)):
                        huts.append(buf[m])
                    buf.clear()
                    
                    for k in range(0,len(cannons)):
                        x1=cannons[k][0]
                        y1=cannons[k][1]
                        
                        if(x1==i and y1==j):
                            #print("theek")
                            
                            cannons[k][2]-=self.damage
                            #cannons[k]=tuple(fg)
                            #buf.append(tuple(fg))
                    for k in range(0,len(wizard_towers)):
                        x1=wizard_towers[k][0]
                        y1=wizard_towers[k][1]
                        
                        if(x1==i and y1==j):
                            #print("theek")
                            
                            wizard_towers[k][2]-=self.damage
                            #cannons[k]=tuple(fg)
                            #buf.append(tuple(fg))
                    
                    for k in range(0,len(th)):
                        x1=th[k][1]
                        y1=th[k][0]
                        #s=0
                        if(x1==i and y1==j):
                            #print("theek")
                            s=1
                            for  l in range(0,len(th)) :
                                
                                th[l][2]-=self.damage
                                    #cannons[k]=tuple(fg)
                                    #buf.append(tuple(fg))
                            #th[k][2]-=self.damage
                            
                            break
                            #cannons[k]=tuple(fg)
                if s==1:
                    break
            if s==1:
                break
        
                            
        if(len(th) != 0 and th[0][2] <= 0):
            th.clear()
        if len(cannons)>0 and cannons[0][2]<=0:
            cannons.pop(0)
        if len(cannons)>1 and cannons[1][2]<=0:
            cannons.pop(1)
        if len(cannons)>2 and cannons[2][2]<=0:
            cannons.pop(2)
        if len(cannons)>3 and cannons[3][2]<=0:
            cannons.pop(3)
        if len(wizard_towers)>0 and wizard_towers[0][2]<=0:
            wizard_towers.pop(0)
        if len(wizard_towers)>1 and wizard_towers[1][2]<=0:
            wizard_towers.pop(1)
        if len(wizard_towers)>2 and wizard_towers[2][2]<=0:
            wizard_towers.pop(2)
        if len(wizard_towers)>3 and wizard_towers[3][2]<=0:
            wizard_towers.pop(3)
        if len(wizard_towers)==0:
            wizard_towers.clear()
            
                


    def move(self, board):
        global max_barb,curr_barb,xx,curr_balloon,max_balloon,curr_archer,max_archer
        char = get_input()
        test = 0
        if self.health <= 0 and curr_barb >= max_barb and curr_archer>=max_archer and curr_balloon>=max_balloon and len(balloons)==0 and len(barbs)==0 and len(archers)==0:
            self.game_over = True
            print("Game Over\n You lost!")
            mystring = "health "
            for i in range(0, int(self.health)):
                mystring = mystring+(Back.RED+' '+Style.RESET_ALL)
            mystring = mystring+" "
            mystring = mystring+str(self.health)+"\n\n"
            mystring+="Level "+str(level)+"\n"
            #buf = "\n".join(["".join(row) for row in self.output])
            mystring = mystring
            mystring = mystring+"\n\nGame Over\n You lost!"
            return 'q'
        
        if char == ' ' and xx==1 and self.health>0:
            # print("kaaaaaajkdksnknksk,")
            buf = []
            for i in range(0, len(bricks)):
                if bricks[i][1] == self.x+1 and bricks[i][0] == self.y:
                    throbricks.append((bricks[i][0], bricks[i][1]))

                if bricks[i][1] == self.x and bricks[i][0] == self.y+1:
                    throbricks.append((bricks[i][0], bricks[i][1]))
                if bricks[i][1] == self.x and bricks[i][0] == self.y-1:
                    throbricks.append((bricks[i][0], bricks[i][1]))
                if bricks[i][1] == self.x-1 and bricks[i][0] == self.y:
                    throbricks.append((bricks[i][0], bricks[i][1]))
            for i in range(0, len(huts)):
                fg = list(huts[i])
                if huts[i][1] == self.x+1 and huts[i][0] == self.y:
                    fg[2] -= self.damage
                    if(fg[2] <= 0):
                        continue

                if huts[i][1] == self.x and huts[i][0] == self.y+1:
                    fg[2] -= self.damage
                    if(fg[2] <= 0):
                        continue
                if huts[i][1] == self.x and huts[i][0] == self.y-1:
                    fg[2] -= self.damage
                    if(fg[2] <= 0):
                        continue
                if huts[i][1] == self.x-1 and huts[i][0] == self.y:
                    fg[2] -= self.damage
                    if(fg[2] <= 0):
                        continue
                fg = tuple(fg)
                buf.append(fg)
            #
            huts.clear()
            for i in range(0, len(buf)):
                huts.append(buf[i])
            # return char
            for i in range(0, len(cannons)):
                #fg = list(huts[i])
                if cannons[i][0] == self.x+1 and cannons[i][1] == self.y:
                    cannons[i][2] -= self.damage
                    

                if cannons[i][0] == self.x and cannons[i][1] == self.y+1:
                    cannons[i][2] -= self.damage
                    
                if cannons[i][0] == self.x and cannons[i][1] == self.y-1:
                    cannons[i][2] -= self.damage
                    
                if cannons[i][0] == self.x-1 and cannons[i][1] == self.y:
                    cannons[i][2] -= self.damage
            if len(cannons)>0 and cannons[0][2]<=0:
                cannons.pop(0)
            if len(cannons)>1 and cannons[1][2]<=0:
                cannons.pop(1)
            if len(cannons)>2 and cannons[2][2]<=0:
                cannons.pop(2)
            if len(cannons)>3 and cannons[3][2]<=0:
                cannons.pop(3)
            
            for i in range(0, len(wizard_towers)):
                #fg = list(huts[i])
                if wizard_towers[i][0] == self.x+1 and wizard_towers[i][1] == self.y:
                    wizard_towers[i][2] -= self.damage
                    

                if wizard_towers[i][0] == self.x and wizard_towers[i][1] == self.y+1:
                    wizard_towers[i][2] -= self.damage
                    
                if wizard_towers[i][0] == self.x and wizard_towers[i][1] == self.y-1:
                    wizard_towers[i][2] -= self.damage
                    
                if wizard_towers[i][0] == self.x-1 and wizard_towers[i][1] == self.y:
                    wizard_towers[i][2] -= self.damage
            if len(wizard_towers)>0 and wizard_towers[0][2]<=0:
                wizard_towers.pop(0)
            if len(wizard_towers)>1 and wizard_towers[1][2]<=0:
                wizard_towers.pop(1)
            if len(wizard_towers)>2 and wizard_towers[2][2]<=0:
                wizard_towers.pop(2)
            if len(wizard_towers)>3 and wizard_towers[3][2]<=0:
                wizard_towers.pop(3)
                
            
            
                
            for i in range(0, len(th)):
                # fg=list(huts[i])
                if th[i][1] == self.x+1 and th[i][0] == self.y:
                    for j in range(0, len(th)):
                        th[j][2] -= self.damage
                    break

                if th[i][1] == self.x and th[i][0] == self.y+1:
                    for j in range(0, len(th)):
                        th[j][2] -= self.damage
                    break
                if th[i][1] == self.x and th[i][0] == self.y-1:
                    for j in range(0, len(th)):
                        th[j][2] -= self.damage
                    break
                if th[i][1] == self.x-1 and th[i][0] == self.y:
                    for j in range(0, len(th)):
                        th[j][2] -= self.damage
                    break

            #
            if(len(th) != 0 and th[0][2] == 0):
                th.clear()

            return char
        elif(char ==' ' and xx==2 and self.health>0):
            self.queen_attack(char)
            return char
        elif (char=='e' and xx==2 and self.health>0):
            t = threading.Timer(1,self.delayed_detection,(char))
            t.start()
            #self.queen_attack(char)
            return char
        if(char == 'd'):
            self.last=char
            for i in range(0, len(bricks)):
                if bricks[i][1] == self.x+1 and bricks[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(cannons)):
                if cannons[i][0] == self.x+1 and cannons[i][1] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(th)):
                if th[i][1] == self.x+1 and th[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char

            for i in range(0, len(huts)):
                if huts[i][1] == self.x+1 and huts[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(spawns)):
                if spawns[i][1] == self.x+1 and spawns[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            if((self.x+self.width-1) < (NUM_COLS-1)):

                move = True

                if(move):
                    self.x = self.x+1

            elif((self.x+self.width-1) < (board.cols-1)):

                move = True

                if(move):
                    self.x = self.x+1

        if(char == 's'):
            self.last=char
            for i in range(0, len(bricks)):
                if bricks[i][1] == self.x and bricks[i][0] == self.y+1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(cannons)):
                if cannons[i][0] == self.x and cannons[i][1] == self.y+1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(th)):
                if th[i][1] == self.x and th[i][0] == self.y+1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(huts)):
                if huts[i][1] == self.x and huts[i][0] == self.y+1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(spawns)):
                if spawns[i][1] == self.x and spawns[i][0] == self.y+1:
                    test = 1
                    break
            if(test == 1):
                return char
            if((self.y) < (NUM_ROWS-1)):

                move = True
                #print(char)

                if(move):
                    self.y = self.y+1

        elif(char == 'w'):
            self.last=char
            for i in range(0, len(bricks)):
                if bricks[i][1] == self.x and bricks[i][0] == self.y-1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(cannons)):
                if cannons[i][1] == self.x and cannons[i][0] == self.y-1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(th)):
                if th[i][1] == self.x and th[i][0] == self.y-1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(huts)):
                if huts[i][1] == self.x and huts[i][0] == self.y-1:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(spawns)):
                if spawns[i][1] == self.x and spawns[i][0] == self.y-1:
                    test = 1
                    break
            if(test == 1):
                return char
            if(self.y > 1):

                move = True

                if(move):
                    self.y = self.y-1

            elif (self.y > 0):

                move = True

                if(move):
                    self.y = self.y-1

        elif(char == 'a'):
            self.last=char
            for i in range(0, len(bricks)):
                if bricks[i][1] == self.x-1 and bricks[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(cannons)):
                if cannons[i][0] == self.x-1 and cannons[i][1] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(th)):
                if th[i][1] == self.x-1 and th[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(huts)):
                if huts[i][1] == self.x-1 and huts[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            for i in range(0, len(spawns)):
                if spawns[i][1] == self.x-1 and spawns[i][0] == self.y:
                    test = 1
                    break
            if(test == 1):
                return char
            if(self.x > 1):

                move = True

                if(move):
                    self.x = self.x-1

            elif (self.x > 0):

                move = True

                if(move):
                    self.x = self.x-1

        elif(char == 'z'):
            if(max_barb>curr_barb):
                Barbarian(27,1)
                curr_barb+=1
        elif char=='x':
            if(max_balloon>curr_balloon):
                Balloon(27,1)
                curr_balloon+=1
        elif char=='c':
            if(max_archer>curr_archer):
                Archer(27,1)
                curr_archer+=1
        
        elif(char == 'u'):
            if(curr_barb<max_barb):
                Barbarian(4,60)
                curr_barb+=1
        elif char=='o':
            if(max_archer>curr_archer):
                Archer(4,60)
                curr_archer+=1
        elif char=='i':
            if(max_balloon>curr_balloon):
                Balloon(4,60)
                curr_balloon+=1
        elif(char == 'm'):
            if(curr_barb<max_barb):
                Barbarian(25,75)
                curr_barb+=1
        elif char=='n':
            if(max_balloon>curr_balloon):
                Balloon(25,75)
                curr_balloon+=1
        elif char=='b':
            if(max_archer>curr_archer):
                Archer(25,75)
                curr_archer+=1
        elif char=='h':
                
            
                

            self.health*=1.5
            if self.health>10:
                self.health=10
            for i in range(0,len(barbs)):
                barbs[i][2]*=1.5
                if barbs[i][2]>3:
                    barbs[i][2]=3
            for i in range(0,len(balloons)):
                balloons[i][2]*=1.5
                if balloons[i][2]>3:
                    balloons[i][2]=3
            for i in range(0,len(archers)):
                archers[i][2]*=1.5
                if archers[i][2]>1.5:
                    archers[i][2]=1.5
        
        #print(curr_barb)
        return char
