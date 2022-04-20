throbricks=[]
huts = []
th=[]
barbs=[]
cannons=[]
wizard_towers=[]
balloons=[]
archers=[]
level=1
xx=0
curr_barb=0
max_barb=15
max_balloon=3
curr_balloon=0
max_archer=3
curr_archer=0
# global variable
 
def th_init():
    for i in range(18,22):
        for j in range(24,27):
            th.append([i,j,5])
    return th
def cs_init():
    cannons.append(35,17,2)
    cannons.append(12,15,2)
    return cannons