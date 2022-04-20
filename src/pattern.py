import random

from time import sleep
from src.wall import Wall
from src.headerss import throbricks
bricks = []
from src.headerss import huts 
spawns = []

class Pattern():

    @staticmethod
    def level_1(cols):
        #ub = UnbreakableBrick(0,0)

        #upper_limit = 8

        x, y = 5, 5

        
        #bricks.append((x,y))

        for i in range(0,30):
            x=10
            y=x+10+i
            bricks.append((x,y))
        for i in range(0,30):
            x=25
            y=x-5+i
            bricks.append((x,y))
        for i in range(0,15):
            y=20
            x=11+i
            bricks.append((x,y))
        for i in range(0,15):
            y=49
            x=11+i
            bricks.append((x,y))
            #sleep(1)
        for i in range (0,len(throbricks)):
            #print(len(bricks))
            #print(throbricks[i][0],throbricks[i][1])
            for j in range(0,len(bricks)):
                if bricks[j][0]==throbricks[i][0] and bricks[j][1]==throbricks[i][1]:
                    bricks.remove((throbricks[i][0],throbricks[i][1]))
                    break
            #print(len(bricks))
            #i+=1
            #sleep(3)
            #throbricks.remove((throbricks[i][0],throbricks[i][1]))
        #throbricks.clear()
        """while True:
            x = random.choice([1, ub.width//2, ub.width//2 + 1])
            while True:
                if((x+ub.width)>=cols):
                    break
                index = random.choice([0,0,0,0,0,1,1,2])
                if(index == 0):
                    bricks.append(EasyBrick(x,y))
                elif(index == 1): 
                    bricks.append(MediumBrick(x,y))
                else:
                    bricks.append(HardBrick(x,y))
                x+=ub.width+1
            y+=ub.height+1
            if(y>=upper_limit):
                break"""
        
        # adding unbreakable bricks
        """ind = random.randint(2,6)
        if(len(bricks) > 6):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(18,20)
        if(len(bricks) > 20):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(35,38)
        if(len(bricks) > 38):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)

        ind = random.choice([13, 24, 29])
        if(len(bricks) > ind):
            bricks[ind] = SuperBrick(bricks[ind].x, bricks[ind].y)

        # for rainbow brick
        filtered_bricks = list(filter(lambda x: type(x) not in [UnbreakableBrick, SuperBrick], bricks))
        
        for brick in random.sample(filtered_bricks, random.randint(4,8)):
            brick.is_rainbow = True"""
        
        return bricks
    
    @staticmethod
    def level_2(cols):
        #ub = UnbreakableBrick(0,0)

        upper_limit = 8

        x, y = 5, 5

        
        
        #bricks.append((x,y))

        x=7
        y=8
        huts.append((x,y,3))
        x=19
        y=70
        huts.append((x,y,3))
        x=8
        y=8
        huts.append((x,y,3))
        x=12
        y=40
        huts.append((x,y,3))
        x=8
        y=7
        huts.append((x,y,3))
        
        """while True:
            x = random.choice([1, ub.width//2, ub.width//2 + 1])
            while True:
                if((x+ub.width)>=cols):
                    break
                index = random.choice([0,0,0,0,0,1,1,2])
                if(index == 0):
                    bricks.append(EasyBrick(x,y))
                elif(index == 1): 
                    bricks.append(MediumBrick(x,y))
                else:
                    bricks.append(HardBrick(x,y))
                x+=ub.width+1
            y+=ub.height+1
            if(y>=upper_limit):
                break"""
        
        # adding unbreakable bricks
        """ind = random.randint(2,6)
        if(len(bricks) > 6):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(18,20)
        if(len(bricks) > 20):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(35,38)
        if(len(bricks) > 38):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)

        ind = random.choice([13, 24, 29])
        if(len(bricks) > ind):
            bricks[ind] = SuperBrick(bricks[ind].x, bricks[ind].y)

        # for rainbow brick
        filtered_bricks = list(filter(lambda x: type(x) not in [UnbreakableBrick, SuperBrick], bricks))
        
        for brick in random.sample(filtered_bricks, random.randint(4,8)):
            brick.is_rainbow = True"""
        
        return huts
    @staticmethod
    def level_3(cols):
        #ub = UnbreakableBrick(0,0)

        upper_limit = 8

        x, y = 5, 5

        
        
        #bricks.append((x,y))

        x=27
        y=1
        spawns.append((x,y))
        x=25
        y=75
        spawns.append((x,y))
        x=4
        y=60
        spawns.append((x,y))
        
        
        """while True:
            x = random.choice([1, ub.width//2, ub.width//2 + 1])
            while True:
                if((x+ub.width)>=cols):
                    break
                index = random.choice([0,0,0,0,0,1,1,2])
                if(index == 0):
                    bricks.append(EasyBrick(x,y))
                elif(index == 1): 
                    bricks.append(MediumBrick(x,y))
                else:
                    bricks.append(HardBrick(x,y))
                x+=ub.width+1
            y+=ub.height+1
            if(y>=upper_limit):
                break"""
        
        # adding unbreakable bricks
        """ind = random.randint(2,6)
        if(len(bricks) > 6):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(18,20)
        if(len(bricks) > 20):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(35,38)
        if(len(bricks) > 38):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)

        ind = random.choice([13, 24, 29])
        if(len(bricks) > ind):
            bricks[ind] = SuperBrick(bricks[ind].x, bricks[ind].y)

        # for rainbow brick
        filtered_bricks = list(filter(lambda x: type(x) not in [UnbreakableBrick, SuperBrick], bricks))
        
        for brick in random.sample(filtered_bricks, random.randint(4,8)):
            brick.is_rainbow = True"""
        
        return spawns

