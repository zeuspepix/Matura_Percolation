#iteration
#import grid_2 as g  #####for sorting
import time
import grid_2_safety_file as g  ####without sorting


    #functions of grid_2
#setup(n) -> return n,b,start
#newgrid(b, start) -> grid
#printgrid(grid, breit, start)
#field(grid, position, tovisit, b, p)
#startinggrid(grid, start)
#removevisited(tovisit)
#onerun(grid, tovisit, b, p) -> has field and removevisited in
    #####################

    #start of programm

size = 500

values = [0.58, 0.5825, 0.585, 0.5875, 0.59, 0.5925, 0.595, 0.5975, 0.6]

iterations = 200

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
    mostart = time.process_time()
    for j in range(iterations):
        g.onerun(grid, tovisit, b, values[i])
#        g.printgrid(grid, b, start)
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
    moend = time.process_time()
    print("p =", values[i], ", nowopens: ", nowopen, ", nowclosed: ", nowclosed, ". Processtime = ", moend-mostart)
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
