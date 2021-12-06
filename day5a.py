import numpy
#infile = open("day5testa.txt", "r")
infile = open("day5input.txt", "r")
lines = infile.readlines()
linepoints = []
maxX = 0
maxY = 0

for line in lines:
    workingline = line.split()
    linepoints.append([workingline[0].split(","), workingline[2].split(",")])
totalpoints = 0
for entry in linepoints:
    print("Point 1")
    print(entry[0])
    if int(entry[0][0]) > maxX:
        maxX = int(entry[0][0])
    if int(entry[0][1]) > maxY:
        maxY = int(entry[0][1])
    print("Point 2")
    print(entry[1])
    if int(entry[1][0]) > maxX:
        maxX = int(entry[1][0])
    if int(entry[1][1]) > maxY:
        maxY = int(entry[1][1])

grid = numpy.zeros(shape=(int(maxX)+1,int(maxY)+1))

print grid
for entry in linepoints:
    print "***"
    #        x2            x1
    if int(entry[1][0]) > int(entry[0][0]):
        print("X direction increase");
        xdir = 1
    #       x1             x2      
    elif int(entry[0][0]) == int(entry[1][0]):
        print("X direction static")
        xdir = 0
    else:
        print("X direction decrease");
        xdir = -1
    #        y2            y1
    if int(entry[1][1]) > int(entry[0][1]):
        print("Y direction increase");
        ydir = 1
    #        y1             y2
    elif int(entry[0][1]) == int(entry[1][1]):
        print("Y direction static")
        ydir = 0
    else:
        print("Y direction decrease");
        ydir = -1

    if (xdir == 0) and (ydir != 0):
        print "Vertical Line"
        #                      y1                y2
        #for y in range(int(entry[0][1]), int(entry[1][1]) + ydir, ydir):
        #    print(y,entry[0][0])
        for y in range(abs(int(entry[1][1]) - int(entry[0][1])) + 1):
        #                  x1, y                      x1, y
            grid[int(entry[0][0]),int(entry[0][1]) + y*ydir] += 1
        totalpoints += abs(int(entry[0][1]) - int(entry[1][1])) + 1
    elif (xdir != 0) and (ydir == 0):
        print "Horizontal Line"
        #                      x1                x2
        #for x in range(int(entry[0][0]), int(entry[1][0]) + xdir, xdir):
        #    print(x,entry[0][1])
        print(entry[0][0], entry[1][0], xdir)
        for x in range(abs(int(entry[1][0]) - int(entry[0][0])) + 1):
        #                      x,y1             x,y1
            grid[int(entry[0][0]) + x*xdir, int(entry[0][1])] += 1
        totalpoints += abs(int(entry[0][0]) - int(entry[1][0])) + 1
    elif (xdir == 0) and (ydir == 0):
        print("**POINT**")
        #grid[ int(entry[0][0]),  int(entry[0][0])] = grid[ int(entry[0][0]),  int(entry[0][0])] + 1
    else:
        print "Diagonal Line"
        for x in range(abs(int(entry[1][0]) - int(entry[0][0])) + 1):
        #                      x,y1             x,y1
            grid[int(entry[0][0]) + x*xdir, int(entry[0][1]) + x*ydir] += 1
            totalpoints += abs(int(entry[0][0]) - int(entry[1][0])) + 1

print grid.transpose()

totalcount = 0
totalgreater1 = 0
for z in range(10):
   count = 0
   for row in grid:
       for val in row:
          if val == z:
              count = count + 1
          if val > 1:
              totalgreater1 += 1
   totalcount += count * z
   print z, count
print len(lines), "lines"
print "Max X", maxX, "Max Y", maxY, "Total Points", int(maxX)*int(maxY)
print totalcount
print totalpoints
print totalgreater1