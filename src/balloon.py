from numpy import rad2deg
from src.barbarian import Barbarian
from src.headerss import huts,th,throbricks,cannons,wizard_towers,balloons
from colorama import Fore, Back, Style 
import random

class Balloon():
    def __init__(self,x,y):
        
        self.health=Barbarian(-1,-1).health
        self.damage=Barbarian(-1,-1).damage*2
        self.x=x
        self.y=y
        self.height = 1
        self.width = 1
        self.pixel3 = Back.LIGHTBLACK_EX+' O'+Style.RESET_ALL
        self.pixel2 = Back.LIGHTCYAN_EX+' O'+Style.RESET_ALL
        self.pixel1 = Back.WHITE+' O'+Style.RESET_ALL
        if x>=0 or y>=0:
            balloons.append([self.x,self.y,self.health])
    
    def move(self):
        for h in range(0,2):
            mini=10000
            minix=10000
            miniy=10000
            keep=0
            
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
            if(len(wizard_towers)!=0 or len(cannons)!=0):
                for i in range(0,len(balloons)):
                    x0=balloons[i][1]
                    y0=balloons[i][0]
                    
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
                    if abs(minix-balloons[i][1])<=0 and abs(miniy-balloons[i][0])<=0  :
                    #print("ok")
                        buf=[]
                        flag=0
                        for j in range(0,len(cannons)):
                    
                            if cannons[j][0]==minix and cannons[j][1]==miniy:
                                cannons[j][2]-=self.damage
                        for j in range(0,len(wizard_towers)):
                    
                            if wizard_towers[j][0]==minix and wizard_towers[j][1]==miniy:
                                wizard_towers[j][2]-=self.damage
                        
                    elif(minix==balloons[i][1]):
                        if miniy<balloons[i][0]:
                            balloons[i][0]-=1
                        elif miniy>balloons[i][0]:
                            balloons[i][0]+=1
                    elif minix>balloons[i][1]:
                        balloons[i][1]+=1
                        #print("done")
                    elif minix<=balloons[i][1]:
                        balloons[i][1]-=1
            else:
                for i in range(0,len(balloons)):
                    x0=balloons[i][1]
                    y0=balloons[i][0]
                    for j in range(0,len(th)):
                        x1=th[j][1]
                        y1=th[j][0]
                        a=min(abs(x1-x0)+abs(y1-y0),mini)
                        if(a<mini):
                            minix=abs(x1)
                            miniy=abs(y1)
                            mini=a
                    for j in range(0,len(huts)):
                        x1=huts[j][1]
                        y1=huts[j][0]
                        a=min(abs(x1-x0)+abs(y1-y0),mini)
                        if(a<mini):
                            minix=abs(x1)
                            miniy=abs(y1)
                            mini=a
                    if abs(minix-balloons[i][1])==0 and abs(miniy-balloons[i][0])==0  :
                    #print("ok")
                        buf=[]
                        flag=0
                        for j in range(0,len(th)):
                    
                            if th[j][1] == minix and th[j][0] == miniy:
                                for j in range(0, len(th)):
                                    th[j][2] -= self.damage
                                if(th[0][2]<=0):
                                    th.clear()
                                break
                        for j in range(0,len(huts)):
                    
                            fg=list(huts[j])
                        #print("theek")
                            if fg[0]==miniy and fg[1]==minix:
                                fg[2]-=self.damage
                                flag=1
                            buf.append(tuple(fg))
                        if flag==1 :
                            huts.clear()
                            for j in range(0,len(buf)):
                                if(buf[j][2]>0):
                                    huts.append(buf[j])
                        
                    elif(minix==balloons[i][1]):
                        if miniy<balloons[i][0]:
                            balloons[i][0]-=1
                        elif miniy>balloons[i][0]:
                            balloons[i][0]+=1
                    elif minix>balloons[i][1]:
                        balloons[i][1]+=1
                        #print("done")
                    elif minix<=balloons[i][1]:
                        balloons[i][1]-=1