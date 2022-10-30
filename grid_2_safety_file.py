#safety save grid_2, without sorting tovisit for closeness to boarder

import random as r
import time

    ##   classes

class site:
    def __init__(self, stelle):
        self.stelle = stelle
        self.visited = False
        self.status = 0    #### 0 unknown, 1 open, 2 closed
        
    def visiting(self):
        self.visited = True
    
    def visitedtest(self):
        return self.visited
    
    def statusopen(self):   #### open   {open() is already a function of python, not a possible private_function :( }
        self.status = 1
        
    def statusclosed(self):   #### closed
        self.status = 2
    
    
    ##  Variabeln

def setup(n):
    b = (2*n)+1
    start = 2*((n**2)+n)
    return n, b, start

#p = 0.51

unendlich = 0


    ##   grid

#n = 20 #grösse der Grid

#b = (2*n)+1
#
#start = 2*((n**2)+n)

def newgrid(b, start):
    grid = [site(i) for i in range(b**2)]
    grid[start].statusopen()
    return grid

def startinggrid(grid, start):
    tovisit = []
    tovisit.append(grid[start])
    return tovisit


#grid = [site(i) for i in range(b**2)]
#tovisit = []

#grid[start].statusopen()

# 0 unbekannt, 1 offen, 2 zu
# False: nicht besucht, True: besucht

def printgrid(grid, breit,start):
    print("here the grid: (", breit, "x", breit, ")")
    for i in range(len(grid)):
        if (i+1)%breit != 0:
            if grid[i].stelle == start:
                print("[X]", end="")
            elif grid[i].status == 1:
                print("[ ]", end="")
            elif grid[i].status == 2:
                print("[#]", end="")
            else:
                print("[0]", end="")
        else:
            if grid[i].stelle == start:
                print("[x]")
            elif grid[i].status == 1:
                print("[ ]")
            elif grid[i].status == 2:
                print("[#]")
            else:
                print("[0]")

    ##    visit

#tovisit.append(grid[start])

def field(grid, position, tovisit, b, p):
    position.visiting()
    Feld = []
    global unendlich
    if (position.stelle-b) < 0: #up
#        print("INFINITE STRIIIIIINNNNGGGGG")
        unendlich += 1
        return tovisit.clear()
    if (position.stelle+b) > (b**2): #down
#        print("INFINITE STRIIIIIINNNNGGGGG")
        unendlich += 1
        return tovisit.clear()
    if ((position.stelle)%b)-1 < 0: #left
#        print("INFINITE STRIIIIIINNNNGGGGG")
        unendlich += 1
        return tovisit.clear()
    if ((position.stelle)+1)% b == 0: #right
#        print("INFINITE STRIIIIIINNNNGGGGG")
        unendlich += 1
        return tovisit.clear()
    if grid[(position.stelle)-b].status == 0:
        Feld.append(grid[(position.stelle)-b]) #up
    if grid[(position.stelle)+b].status == 0:
        Feld.append(grid[(position.stelle)+b]) #down
    if grid[(position.stelle)-1].status == 0:
        Feld.append(grid[(position.stelle)-1]) #left
    if grid[(position.stelle)+1].status == 0:
        Feld.append(grid[(position.stelle)+1]) #right
    for i in range(len(Feld)):
        rr = r.random()
        if rr <= p:
            Feld[i].statusopen()
        else:
            Feld[i].statusclosed()
    for i in range(len(Feld)):
        if Feld[i].status == 1:
            tovisit.append(grid[(Feld[i].stelle)])
        
def removevisited(tovisit):
    toremove = []
    for i in range(len(tovisit)):
        if tovisit[i].visitedtest() == True:
            toremove.append(i)
    for j in range(len(toremove)):
        tovisit.pop(toremove[j])

def onerun(grid, tovisit, b, p):
    while len(tovisit) > 0:
        field(grid, tovisit[-1], tovisit, b, p)
        removevisited(tovisit)
#    if unendlich == 0:
#        print("no infinite string :(")
        
        
        #tests


#begin = time.process_time()

#while len(tovisit) > 0:
#    field(tovisit[-1])
#    removevisited()
#    for i in range(len(tovisit)): 
#        print(tovisit[i].stelle, tovisit[i].status) 
      
#end = time.process_time()      

#if unendlich == 0:
#    print("no infinite string :(")

#print(end-begin)

#   test
#for f in range(len(grid)):
#    if grid[f].status == 1:
#        print(grid[f].stelle, grid[f].status)


#print("here the grid: (", b, "x", b, ")")
#for i in range(len(grid)):
#    if (i+1)%b != 0:
#        if grid[i].stelle == start:
#            print("[X]", end="")
#        elif grid[i].status == 1:
#            print("[ ]", end="")
#        elif grid[i].status == 2:
#            print("[#]", end="")
#        else:
#            print("[0]", end="")
#    else:
#        if grid[i].stelle == start:
#            print("[x]")
#        elif grid[i].status == 1:
#            print("[ ]")
#        elif grid[i].status == 2:
#            print("[#]")
#        else:
#            print("[0]")


if __name__ == "__main__":
    print("hello!")
    