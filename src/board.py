from cmath import sqrt
from operator import le
from colorama import Fore, Back, Style
from os import system
import random
from time import sleep, time
import math

from colorama import Fore, Back, Style
from os import system

from matplotlib.pyplot import bar
from src.king import King
from src.wall import Wall
from src.huts import Hut
from src.archer import Archer
from src.townhall import Townhall
from src.spawning import Spawning
from src.cannon import Cannon, Wizard_Tower
from src.headerss import huts
from src.headerss import th_init
import random
from time import sleep, time
import math
from src.pattern import Pattern
from src.headerss import throbricks
from src.headerss import th,level
from src.headerss import barbs, cannons, wizard_towers,balloons,archers
from src.barbarian import Barbarian
from src.headerss import max_barb, curr_barb,xx,curr_archer,max_archer,max_balloon,curr_balloon
from src.balloon import Balloon
class Board():
    #global level


    def __init__(self, balls=[]):
        global level,throbricks,cannons,wizard_towers,th,barbs,huts,max_barb,curr_barb
        #global level
        #curr_barb=0
        self.cols = 80
        self.rows = 31
        self.king = King(0, 0)
        #self.queen=King(0,0)
        self.barbarian = Barbarian(-1, -1)
        self.balloon = Balloon(-1, -1)
        self.archer=Archer(-1, -1)
        self.score = 0
        self.hut = Hut(0, 0)
        self.spawn = Spawning(0, 0)
        self.townhall = Townhall(24, 18)
        self.cannon1 = Cannon(7, 0.5, 35, 17)
        self.cannon2 = Cannon(7, 0.5, 12, 15)
        self.wt1 = Wizard_Tower(7, 0.5, 73, 8)
        self.wt2 = Wizard_Tower(7, 0.5, 60, 23)
        if level == 2:
            self.cannon3 = Cannon(7, 0.5, 35, 10)
            self.wt3 = Wizard_Tower(7, 0.5, 14, 8)
        if level == 3:
            self.cannon3 = Cannon(7, 0.5, 35, 10)
            self.wt3 = Wizard_Tower(7, 0.5, 14, 8)
            self.cannon4 = Cannon(7, 0.5, 42, 20)
            self.wt4 = Wizard_Tower(7, 0.5, 52, 19)
        self.ths = th_init()
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.startTime = time()
        self.currentTime = time()
        self.barb = barbs

        self.game_over = False
        # self.ekbarb=Barbarian(0,0)

        self.ticks = 0
        self.boss = None
        self.walls = Pattern.level_1(self.cols)
        self.huts = Pattern.level_2(self.cols)
        self.spawns = Pattern.level_3(self.cols)
        self.render()
    def initialise(self):
        global level,throbricks,cannons,wizard_towers,th,barbs,huts,max_barb,curr_barb,xx,curr_archer,max_archer,max_balloon,curr_balloon
        
        self.king = King(0, 0)
        self.barbarian = Barbarian(-1, -1)
        throbricks.clear()
        self.score = 0
        self.walls = Pattern.level_1(self.cols)
        huts.clear()
        huts = Pattern.level_2(self.cols)
        cannons.clear()
        
        barbs.clear() 
        balloons.clear()
        archers.clear()
        #curr_barb=0
        wizard_towers.clear()
        th.clear()
        self.game_over = False
        
        th=th_init()
        self.hut = Hut(0, 0)
        #self.spawn = Spawning(0, 0)
        #self.townhall = Townhall(24, 18)
        self.cannon1 = Cannon(7, 0.5, 35, 17)
        self.cannon2 = Cannon(7, 0.5, 12, 15)
        self.wt1 = Wizard_Tower(7, 0.5, 73, 8)
        self.wt2 = Wizard_Tower(7, 0.5, 60, 23)
        if level >= 2:
            self.cannon3 = Cannon(7, 0.5, 35, 8)
            self.wt3 = Wizard_Tower(7, 0.5, 14,5)
        if level == 3:
            #self.cannon3 = Cannon(7, 0.5, 35, 10)
            self.wt4 = Wizard_Tower(7, 0.5, 21, 8)
            self.cannon4 = Cannon(7, 0.5, 42, 20)
    def render(self):
        system('clear')
        global level,throbricks,cannons,wizard_towers,th,barbs,huts,curr_barb,max_barb,xx,curr_archer,max_archer,max_balloon,curr_balloon
        self.board = [[self.bg_pixel for i in range(
            self.cols)] for j in range(self.rows)]

        """for brick in self.walls:
            print(brick)
            for row in range(brick., brick.y+1):
                for col in range(brick.x, brick.x+1):
                    self.board[row][col] = Back.BLACK+' '+Style.RESET_ALL"""

        # adding borders to board
        score_board_height = 0
        wall = 1
        border_pixel = Back.GREEN+'  '+Style.RESET_ALL

        self.output = [[border_pixel for i in range(
            self.cols)] for j in range(self.rows)]

        """title = "Clash of Clans"
        title_offset = (self.cols+wall-len(title)) // 2
        for j in range(0, len(title)):
            self.output[1][title_offset+j] = Back.WHITE+Fore.RED+title[j]+Style.RESET_ALL"""

        """score_text = "Score: {}".format(self.score)
        score_text_offset = (self.cols+wall-len(score_text)) // 8
        for j in range(0, len(score_text)):
            self.output[3][score_text_offset+j] = Back.BLUE+Fore.RED+score_text[j]+Style.RESET_ALL"""

        time_elpsed = math.floor(self.currentTime-self.startTime)
        time_taken = "Time: {} seconds".format(time_elpsed)
        time_taken_offset = (self.cols+wall-len(time_taken)) * 3 // 8
        """for j in range(0, len(time_taken)):
            self.output[3][time_taken_offset+j] = Back.WHITE+Fore.RED+time_taken[j]+Style.RESET_ALL"""
        #self.walls = Pattern.level_1(self.cols)
        for i in range(0, len(throbricks)):
            # print(len(bricks))
            # print(throbricks[i][0],throbricks[i][1])
            for j in range(0, len(self.walls)):
                if self.walls[j][0] == throbricks[i][0] and self.walls[j][1] == throbricks[i][1]:
                    self.walls.remove((throbricks[i][0], throbricks[i][1]))
                    break
        """for row in range(self.townhall.y, self.townhall.y+self.townhall.height):
            for col in range(self.townhall.x, self.townhall.x+self.townhall.width):
                self.output[row][col] = self.townhall.pixel"""
        self.ths = th
        tbrb = []
        tb=[]
        atk = 0
        for i in range(0, len(wizard_towers)):
            tbrb = []
            tb=[]
            ta=[]
            all_troops=barbs+balloons+archers
            for j in range(0, len(all_troops)):
                if abs(all_troops[j][1]-wizard_towers[i][0]) + abs(all_troops[j][0]-wizard_towers[i][1]) <= self.wt1.range:
                    # print("sahi")
                    all_troops[j][2] -= self.wt1.damage_val
                    if j<len(barbs):
                        barbs[j][2]-=self.wt1.damage_val
                    elif j>=len(barbs) and j<len(barbs)+len(balloons):
                        balloons[j-len(barbs)][2]-=self.wt1.damage_val
                    elif j>= len(barbs)+len(balloons) and j<len(all_troops):
                        archers[j-len(barbs)-len(balloons)][2]-=self.wt1.damage_val
                    atk = 1
                    for k in range(0,len(all_troops)):
                        if k==j:
                            continue
                        
                        if math.sqrt(abs(all_troops[k][0]-all_troops[j][0])**2+abs(all_troops[k][1]-all_troops[j][1])**2)<1.5:
                            all_troops[k][2] -= self.wt1.damage_val
                            if k<len(barbs):
                                barbs[k][2]-=self.wt1.damage_val
                                if barbs[k][2]<=0:
                                    tbrb.append(k)
                            elif k>=len(barbs) and k<len(barbs)+len(balloons):
                                balloons[k-len(barbs)][2]-=self.wt1.damage_val
                                if balloons[k-len(barbs)][2]<=0:
                                    tb.append(k-len(barbs))
                            elif k>= len(barbs)+len(balloons) and k<len(all_troops):
                                archers[k-len(barbs)-len(balloons)][2]-=self.wt1.damage_val
                                if archers[k-len(barbs)-len(balloons)][2]<=0:
                                    ta.append(k-len(barbs)-len(balloons))
                                #print(math.sqrt(abs(barbs[k][0]-barbs[j][0])**2+abs(barbs[k][1]-barbs[j][1])**2))
                            
                                
                            
                    if j<len(barbs) and barbs[j][2] <= 0:
                        tbrb.append(j)
                    if j<len(barbs)+len(balloons) and j>=len(barbs) and balloons[j-len(barbs)][2] <= 0:
                        tb.append(j-len(barbs))
                    if j<len(barbs)+len(balloons)+len(archers) and j>=len(barbs)+len(balloons) and archers[j-len(barbs)-len(balloons)][2] <= 0:
                        ta.append(j-len(barbs)-len(balloons))
                    break
            if len(barbs)>0:
                for j in range(0, len(tbrb)):
                    print(tbrb[j])
                    if len(barbs)>tbrb[j]:
                        barbs.pop(tbrb[j])
                    #barbs.pop(tbrb[j])
            if len(balloons)>0:
                for j in range(0, len(tb)):
                    balloons.pop(tb[j])
            if len(archers)>0:
                for j in range(0, len(ta)):
                    archers.pop(ta[j])

        for i in range(0, len(cannons)):
            tbrb = []
            ta=[]
            for j in range(0, len(barbs)):
                if abs(barbs[j][1]-cannons[i][0]) + abs(barbs[j][0]-cannons[i][1]) <= self.cannon1.range:
                    # print("sahi")
                    barbs[j][2] -= self.cannon1.damage_val
                    atk = 1
                    if barbs[j][2] <= 0:
                        tbrb.append(j)
                    break
            for j in range(0, len(tbrb)):
                barbs.pop(tbrb[j])
            if atk==0:
                for j in range(0, len(archers)):
                    if abs(archers[j][1]-cannons[i][0]) + abs(archers[j][0]-cannons[i][1]) <= self.cannon1.range:
                        # print("sahi")
                        archers[j][2] -= self.cannon1.damage_val
                        atk = 1
                        if archers[j][2] <= 0:
                            ta.append(j)
                        break
                for j in range(0, len(ta)):
                    archers.pop(ta[j])

        for i in range(0, len(th)):
            if th[i][2] <= 5 and th[i][2]>4:
                self.output[th[i][0]][th[i][1]] = self.townhall.pixel5
            if th[i][2] <= 4 and th[i][2]>3:
                self.output[th[i][0]][th[i][1]] = self.townhall.pixel4
            if th[i][2] <= 3 and th[i][2]>2:
                self.output[th[i][0]][th[i][1]] = self.townhall.pixel3
            if th[i][2] <= 2 and th[i][2]>1:
                self.output[th[i][0]][th[i][1]] = self.townhall.pixel2
            if th[i][2] <= 1 and th[i][2]>0:
                self.output[th[i][0]][th[i][1]] = self.townhall.pixel1
        for index, tuple in enumerate(self.walls):
            row = tuple[0]
            col = tuple[1]
            self.output[row][col] = Back.BLACK+' W'+Style.RESET_ALL
        """for index,tuple in enumerate(self.huts):
            row=tuple[0]
            col=tuple[1]
            self.output[row][col] = self.hut.pixel
            self.output[row][col+1] = self.hut.pixel"""
        self.huts = huts
        for index, tuple in enumerate(self.huts):
            for row in range(tuple[0], tuple[0]+self.hut.height):
                for col in range(tuple[1], tuple[1]+self.hut.width):
                    if tuple[2] <= 3 and tuple[2]>2:
                        self.output[row][col] = self.hut.pixel3
                    if tuple[2] <= 2 and tuple[2]>1:
                        self.output[row][col] = self.hut.pixel2
                    if tuple[2] <= 1 and tuple[2]>0:
                        self.output[row][col] = self.hut.pixel1
        for index, tuple in enumerate(self.spawns):
            for row in range(tuple[0], tuple[0]+self.spawn.height):
                for col in range(tuple[1], tuple[1]+self.spawn.width):
                    self.output[row][col] = self.spawn.pixel
        for j in range(0, len(cannons)):
            if self.king.health > 0 and (abs(self.king.x-cannons[j][0]) + abs(self.king.y-cannons[j][1]) <= self.cannon2.range):
                self.king.health -= self.cannon1.damage_val
                atk = 1
        for j in range(0, len(wizard_towers)):
            if self.king.health > 0 and (abs(self.king.x-wizard_towers[j][0]) + abs(self.king.y-wizard_towers[j][1]) <= self.wt2.range):
                self.king.health -= self.wt1.damage_val
                atk = 1

        if self.king.health > 0:
            for row in range(self.king.y, self.king.y+self.king.height):
                for col in range(self.king.x, self.king.x+self.king.width):
                    self.output[row][col] = self.king.pixel

        for i in range(0, len(cannons)):
            if cannons[i][2] <= 2 and cannons[i][2] > 1:
                self.output[cannons[i][1]][cannons[i][0]] = self.cannon1.pixel2
            if cannons[i][2] <= 1 and cannons[i][2] > 0:
                self.output[cannons[i][1]][cannons[i][0]] = self.cannon1.pixel1

        for i in range(0, len(wizard_towers)):
            if wizard_towers[i][2] <= 2 and wizard_towers[i][2] > 1:
                self.output[wizard_towers[i][1]
                            ][wizard_towers[i][0]] = self.wt1.pixel2
            if wizard_towers[i][2] <= 1 and wizard_towers[i][2] > 0:
                self.output[wizard_towers[i][1]
                            ][wizard_towers[i][0]] = self.wt1.pixel1
        """for row in range(self.cannon1.y, self.cannon1.y+self.cannon1.height):
            for col in range(self.cannon1.x, self.cannon1.x+self.cannon1.width):
                self.output[row][col] = self.cannon1.pixel
        for row in range(self.cannon2.y, self.cannon2.y+self.cannon2.height):
            for col in range(self.cannon2.x, self.cannon2.x+self.cannon2.width):
                self.output[row][col] = self.cannon2.pixel"""
        self.barb = barbs
        for i in range(0, len(barbs)):
            if barbs[i][2] <= 3 and barbs[i][2] > 2:
                self.output[barbs[i][0]][barbs[i][1]
                                        ] = Back.LIGHTBLACK_EX+' B'+Style.RESET_ALL
            if barbs[i][2] <= 2 and barbs[i][2] > 1:
                self.output[barbs[i][0]][barbs[i][1]
                                        ] = Back.LIGHTCYAN_EX+' B'+Style.RESET_ALL
            if barbs[i][2] <= 1 and barbs[i][2] > 0:
                self.output[barbs[i][0]][barbs[i][1]
                                        ] = Back.WHITE+' B'+Style.RESET_ALL
        for i in range(0, len(archers)):
            
            if archers[i][2] <= 2 and archers[i][2] > 1:
                self.output[archers[i][0]][archers[i][1]
                                        ] = Archer(-1,-1).pixel2
            if archers[i][2] <= 1 and archers[i][2] > 0:
                self.output[archers[i][0]][archers[i][1]
                                        ] = Archer(-1,-1).pixel1
        for i in range(0, len(balloons)):
            if balloons[i][2] <= 3 and balloons[i][2] > 2:
                self.output[balloons[i][0]][balloons[i][1]
                                        ] = Balloon(-1,-1).pixel3
            if balloons[i][2] <= 2 and balloons[i][2] > 1:
                self.output[balloons[i][0]][balloons[i][1]
                                        ] = Balloon(-1,-1).pixel2
            if balloons[i][2] <= 1 and balloons[i][2] > 0:
                self.output[balloons[i][0]][balloons[i][1]
                                        ] = Balloon(-1,-1).pixel1

        print("health", end=' ')
        # print("\n")
        for i in range(0, int(self.king.health)):
            print(Back.RED+'                '+Style.RESET_ALL, end='')
        print(self.king.health)
        print("\n")
        print("Level "+str(level))
        #print(str(max_barb)+" "+str(curr_barb))
        #print(curr_barb)

        print("\n".join(["".join(row) for row in self.output]))
        # print("\n")

        #print("\n".join(["".join(row) for row in pr_health]))
        if len(huts) == 0 and len(th) == 0 and len(cannons) == 0 and len(wizard_towers) == 0 and (level ==1 or level==2):
            #self.game_over=True
            level += 1
            print("Game Over\n You won!")
            mystring = "health "
            for i in range(0, int(self.king.health)):
                mystring = mystring+(Back.RED+' '+Style.RESET_ALL)
            mystring = mystring+" "
            mystring = mystring+str(self.king.health)+"\n\n"
            mystring+="Level "+str(level)+"\n"
            buf = "\n".join(["".join(row) for row in self.output])
            mystring = mystring+buf
            mystring = mystring+"\nGame Over\n You won!"
            
            self.initialise()
            King.set_curr_barb(King)
            sleep(2)
            
            #Board().__init__()
        elif len(huts) == 0 and len(th) == 0 and len(cannons) == 0 and len(wizard_towers) == 0 and level == 3:
            self.game_over = True
            # level+=1
            print("Game Over\n You won!")
            mystring = "health "
            for i in range(0, int(self.king.health)):
                mystring = mystring+(Back.RED+' '+Style.RESET_ALL)
            mystring = mystring+" "
            mystring = mystring+str(self.king.health)+"\n\n"
            mystring+="Level "+str(level)+"\n"
            buf = "\n".join(["".join(row) for row in self.output])
            mystring = mystring+buf
            mystring = mystring+"\nGame Over\n You won!"
            sleep(2)
            
            
        elif self.king.health <= 0 and curr_barb >= max_barb and curr_archer>=max_archer and curr_balloon>=max_balloon and len(balloons)==0 and len(barbs)==0 and len(archers)==0:
            self.game_over = True
            print("Game Over\n You lost!")
            mystring = "health "
            for i in range(0, int(self.king.health)):
                mystring = mystring+(Back.RED+' '+Style.RESET_ALL)
            mystring = mystring+" "
            mystring = mystring+str(self.king.health)+"\n\n"
            mystring+="Level "+str(level)+"\n"
            buf = "\n".join(["".join(row) for row in self.output])
            mystring = mystring+buf
            mystring = mystring+"\n\nGame Over\n You lost!"
        else:
            mystring = "health "
            for i in range(0, int(self.king.health)):
                mystring = mystring+(Back.RED+' '+Style.RESET_ALL)
            mystring = mystring+" "
            mystring = mystring+str(self.king.health)+"\n\n"
            mystring+="Level "+str(level)+"\n"
            buf = "\n".join(["".join(row) for row in self.output])
            mystring = mystring+buf

        return (mystring, self.game_over,level)
