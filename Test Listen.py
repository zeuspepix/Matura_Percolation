#Test Percolation erste

import random as r

def control(x):
    if x == 2:
        return False
    else:
        return True
            

n = 10 #n-Dimesionen der Grid
p = 0.5 #p dass die werte [][][2] = 1, sonst = 0
position = n

#feld = [[[i, j] for j in range(-3,4)] for i in range(-3,4)]  ##TEST GRID
#print("feld", feld)

grid = [[[i, j, 0, 0] for i in range(-(n),(n+1))] for j in range(n,-(n+1),-1)] #list comprehension vom Grid

grid[n][n][2] = 1 #Origin muss Teil vom unendlichen strang -> [n][n][2] = 1 (offen)
grid[n][n][3] = 1 #Sackgassenparameter -> 0 nicht entdeckt, 1 offen (für jetzt), 2 SACKGASSE

print(grid)

# start at grid[3][3] hence (0,0)

for i in range(-1,2): #random y variation
    if i == 0:
        for j in range(-1, 2):
            rr = r.random()
            if rr >= 0.5:
                ff = 1
            else:
                ff = 0
            grid[n][n-j][2] = ff
            grid[n][n-j][3] = 1
    else:             #random x variation
        rr = r.random()
        if rr >= 0.5:
            ff = 1
        else:
            ff = 0
        grid[n-i][n][2] = ff
        grid[n-i][n][3] = 1
print("umgebung von (0,0): ", grid[n][n-1], grid[n][n+1], grid[n-1][n], grid[n+1][n])

possible = []

grid[n+1][n][3] = 2

for i in range(-1,2): #random y variation
    if position - i != position:
        if control(grid[n][n-i][3]) == True:
            possible.append(grid[n][n-i])
            False
        if control(grid[n-i][n][3]) == True:
            possible.append(grid[n-i][n])
            False
print("mögliche: ", possible, grid[n-1][n][3])


















        