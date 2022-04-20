from src.barbarian import Barbarian
from src.headerss import huts,th,throbricks,cannons,wizard_towers,archers,throbricks
from src.pattern import Pattern,bricks,spawns
from colorama import Fore, Back, Style 
import random

class Archer():
    def __init__(self,x,y):
        
        self.health=Barbarian(-1,-1).health/2
        self.damage=Barbarian(-1,-1).damage/2
        self.pixel2 = Back.LIGHTCYAN_EX+' A'+Style.RESET_ALL
        self.pixel1 = Back.WHITE+' A'+Style.RESET_ALL
        self.height = 1
        self.width = 1
        self.x=x    
        self.y=y
        self.range=7
        if x>=0 or y>=0:
            archers.append([self.x,self.y,self.health])
    
    def move(self):
        if(len(th)==0 and len(huts)==0 and len(cannons)==0 and len(wizard_towers)==0):
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
        keep=0
    
        #for i in range(0,len(archers)):
            
        if keep==1:
            return
        for i in range(0, len(archers)):
            tbrb = []
            buf=[]
            atk=0
            
            
            for j in range(0, len(cannons)):
                if abs(archers[i][1]-cannons[j][0]) + abs(archers[i][0]-cannons[j][1]) <= self.range:
                    # print("sahi")
                    cannons[j][2] -= self.damage
                    atk = 1
                    break
            if atk==1:
                continue
            for j in range(0, len(wizard_towers)):
                if abs(archers[i][1]-wizard_towers[j][0]) + abs(archers[i][0]-wizard_towers[j][1]) <= self.range and atk==0:
                    # print("sahi")
                    wizard_towers[j][2] -= self.damage
                    atk = 1
                    break
            if atk==1:
                continue
            for j in range(0, len(huts)):
                fg=list(huts[j])
                if abs(archers[i][1]-fg[1]) + abs(archers[i][0]-fg[0]) <= self.range and atk==0 :
                    # print("sahi")
                    fg[2] -= self.damage
                    atk = 1
                buf.append(tuple(fg))
            if atk==1:
                huts.clear()
                for k in range(0,len(buf)):
                    if(buf[k][2]>0):
                        huts.append(buf[k])
                buf.clear()
                continue
            for j in range(0, len(th)):
                #fg=list(th[j])
                if abs(archers[i][1]-th[j][1]) + abs(archers[i][0]-th[j][1]) <= self.range and atk==0 :
                    # print("sahi")
                    
                    atk = 1
                    for j in range(0, len(th)):
                        th[j][2] -= self.damage
                    if(th[0][2]<=0):
                        th.clear()
                    break
            if atk==1:
                continue
            
            if atk==0:
                for j in range(0,len(bricks)):
                    f=list(bricks[j])
                    if  abs(f[0]-archers[i][0]) + abs(f[1]-archers[i][1])==1 or abs(f[0]-archers[i][0])+ abs(f[1]-archers[i][1])==1 or abs(f[0]-archers[i][0])+ abs(f[1]-archers[i][1])==0  :
                        throbricks.append((f[0],f[1]))
                        keep=1
                        break
                if keep==1:
                    continue
                for h in range(0,2):
                    mini=10000
                    minix=10000
                    miniy=10000
                    #for i in range(0,len(barbs)):
                    x0=archers[i][1]
                    y0=archers[i][0]
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
                    
                    if(minix==archers[i][1]):
                        if miniy<archers[i][0]:
                            archers[i][0]-=1
                        elif miniy>archers[i][0]:
                            archers[i][0]+=1
                    elif minix>archers[i][1]:
                        archers[i][1]+=1
                        #print("done")
                    elif minix<=archers[i][1]:
                        archers[i][1]-=1
            
                        
                            
