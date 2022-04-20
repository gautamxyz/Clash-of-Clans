from src.cannon import Wizard_Tower
from src.input import get_input
from colorama import Fore, Back, Style 
import random
from src.pattern import Pattern,bricks,spawns
from src.headerss import barbs
from src.headerss import huts,th,throbricks,cannons,wizard_towers
from time import sleep
#from src.board import Cannon
class Barbarian():

    def __init__ (self,x,y):
        self.health=3
        self.x=x-1
        self.y=y
        self.height = 1
        self.width = 1
        self.damage=0.25
        self.pixel3 = Back.LIGHTBLACK_EX+' B'+Style.RESET_ALL
        self.pixel2 = Back.LIGHTCYAN_EX+' B'+Style.RESET_ALL
        self.pixel1 = Back.WHITE+' B'+Style.RESET_ALL
        if x>=0 or y>=0:
            barbs.append([self.x,self.y,self.health])
        self.speed=1



    def move(self):
        mini=10000
        minix=10000
        miniy=10000
        keep=0
        
        if(len(th)==0 and len(huts)==0 and len(cannons)==0 and len(wizard_towers)==0):
            return
        for i in range(0,len(barbs)):
            for j in range(0,len(bricks)):
                f=list(bricks[j])
                if abs(f[0]-barbs[i][0])==1 and abs(f[1]-barbs[i][1])==0 or abs(f[0]-barbs[i][0])==0 and abs(f[1]-barbs[i][1])==1 :
                    throbricks.append((f[0],f[1]))
                    keep=1
        if keep==1:
            return
        
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
        for i in range(0,len(barbs)):
            x0=barbs[i][1]
            y0=barbs[i][0]
            for j in range(0,len(huts)):
                x1=huts[j][1]
                y1=huts[j][0]
                a=min(abs(x1-x0)+abs(y1-y0),mini)
                if(a<mini):
                    minix=abs(x1)
                    miniy=abs(y1)
                    mini=a
            for j in range(0,len(cannons)):
                x1=cannons[j][0]
                y1=cannons[j][1]
                a=min(abs(x1-x0)+abs(y1-y0),mini)
                if(a<mini):
                    minix=abs(x1)
                    miniy=abs(y1)
                    mini=a
            for j in range(0,len(wizard_towers)):
                x1=wizard_towers[j][0]
                y1=wizard_towers[j][1]
                a=min(abs(x1-x0)+abs(y1-y0),mini)
                if(a<mini):
                    minix=abs(x1)
                    miniy=abs(y1)
                    mini=a
            for j in range(0,len(th)):
                x1=th[j][1]
                y1=th[j][0]
                a=min(abs(x1-x0)+abs(y1-y0),mini)
                if(a<mini):
                    minix=(x1)
                    miniy=(y1)
                    mini=a
            if abs(minix-barbs[i][1])<=1 and abs(miniy-barbs[i][0])<=0 or abs(minix-barbs[i][1])<=0 and abs(miniy-barbs[i][0])<=1 :
                #print("ok")
                buf=[]
                flag=0
                for j in range(0,len(cannons)):
            
                    if cannons[j][0]==minix and cannons[j][1]==miniy:
                        cannons[j][2]-=self.damage
                for j in range(0,len(wizard_towers)):
            
                    if wizard_towers[j][0]==minix and wizard_towers[j][1]==miniy:
                        wizard_towers[j][2]-=self.damage
                for i in range(0,len(huts)):
                    fg=list(huts[i])
                    #print("theek")
                    if fg[0]==miniy and fg[1]==minix:
                        fg[2]-=self.damage
                        flag=1
                    buf.append(tuple(fg))
                if flag==1 :
                    huts.clear()
                    for i in range(0,len(buf)):
                        if(buf[i][2]>0):
                            huts.append(buf[i])
                else :
                    for i in range(0, len(th)):
                # fg=list(huts[i])
                        if th[i][1] == minix and th[i][0] == miniy:
                            for j in range(0, len(th)):
                                th[j][2] -= self.damage
                            if(th[0][2]<=0):
                                th.clear()
                            break
                #print(self.damage)
            elif(minix==barbs[i][1]):
                if miniy<barbs[i][0]:
                    barbs[i][0]-=1
                elif miniy>barbs[i][0]:
                    barbs[i][0]+=1
            elif minix>barbs[i][1]:
                barbs[i][1]+=1
                #print("done")
            elif minix<=barbs[i][1]:
                barbs[i][1]-=1
                
            
        
        