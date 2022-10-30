#functional Iteretion (without sorting)
import grid_2_safety_file as g
import time

    #functions of grid_2
#setup(n) -> return n,b,start
#newgrid(b, start) -> grid
#printgrid(grid, breit, start) -> prints grid
#field(grid, position, tovisit, b, p) -> determines state
#startinggrid(grid, start) -> tovisit with only start
#removevisited(tovisit) -> tovisit minus the visited sites
#onerun(grid, tovisit, b, p) -> executes field and removevisited
    #####################

    #start of programm

size = 10

values = [0.6]

iterations = 1

n, b, start = g.setup(size)

grid = g.newgrid(b, start)
tovisit = g.startinggrid(grid, start)

#g.onerun(grid, tovisit, b, p)
#g.printgrid(grid, b, start)

closedruns = 0
openruns = 0

partopen = []
partclosed = []


starttime = time.process_time()

for i in range(len(values)):
    nowopen = 0
    nowclosed = 0
    for j in range(iterations):
        g.onerun(grid, tovisit, b, values[i])
        g.printgrid(grid, b, start)
        if g.unendlich == 0:
            closedruns += 1
            nowclosed += 1
        else:
            openruns += 1
            nowopen += 1
        g.unendlich = 0
        grid.clear()
        grid = g.newgrid(b, start)
        tovisit = g.startinggrid(grid, start)
    print("p =", values[i], ", nowopens: ", nowopen, ", nowclosed: ", nowclosed)
    if nowclosed == 0:
        partopen.append(values[i])
    elif nowopen/nowclosed > 0.5:
        partopen.append(values[i])
    else:
        partclosed.append(values[i])

endtime = time.process_time()

print()
print("data (", iterations*(len(values)), "runs ) for", b, "X", b, "grid")
print("closedruns: ", closedruns, ";", partclosed, "where mostly closed")
print("openruns: ", openruns, ";", partopen, "where mostly open")

if (endtime-starttime) >= 3600:
    print("processing time:", endtime-starttime, "seconds , ca.", round((endtime-starttime)//3600, 1), "hours and", round(((endtime-starttime)%3600)//60), "minutes")
else:
    print("processing time:", endtime-starttime, "seconds , ca.", round((endtime-starttime)//60), "minutes and", (endtime-starttime)%60, "seconds")
