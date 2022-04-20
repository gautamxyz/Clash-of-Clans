from os import system
from time import sleep
print("Enter the name of the replay file:")

naam=str(input())

f = open("replays/"+naam, "r")

content=f.read().split(',')
system('clear')
for i in range(0,len(content)-1):
    system('clear')
    print(content[i])
    sleep(0.1)
    