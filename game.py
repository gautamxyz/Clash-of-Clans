from src.input import get_input
from src.board import Board
import time
from datetime import datetime
from src.barbarian import Barbarian
from src.king import King
from src.headerss import level,xx

while 1:
    print("Press 1 for king, 2 for queen:")
    xx=int(input())
    if xx==1 or xx==2:
        break
King.set_xx(King,xx)
board = Board()
print(board.rows)
#exit
nam=datetime.now()
naam=str(nam)
f = open("replays/"+naam+".txt", "a")
r=1
if xx==2:
    King(0,0).damage=King(0,0).damage/2


if level==1:
    while(True):
        #getinput
        flag=0
        #check =board.king.move(board)
        board.king.damage=board.king.damage*r 
        board.barbarian.damage=board.barbarian.damage*r
        board.archer.damage=board.archer.damage*r
        board.balloon.damage=board.balloon.damage*r
        
        check=board.king.move(board)
        if check=='q':
            flag=1
        if check=='r':
            r=r*2
        if(check == 'q'):
            break
        x=board.render()
        level=x[2]
        f.write(x[0])
        f.write(',')
        if x[1] == True:
            break
        board.barbarian.move()
        board.balloon.move()
        board.archer.move()
        #Barbarian.move(Barbarian)

        time.sleep(0.05/r)
        #if board.render() == True:
        #   break
