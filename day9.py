import numpy
infile = open("day9input.txt", "r")
lines = infile.readlines()

lowlist = []
for i,line in enumerate(lines):
    print "line ",i
    line = line.strip()
    for n in range(len(line)):
        print line[n]
        #first row
        if(i == 0):
            #first col
            if(n == 0):
                if(lines[i][n] < lines[i][n+1]) and (lines[i][n] < lines[i+1][n]):
                    lowlist.append( (i,n) )
            #last col
            elif(n == len(line) -1):
                if(lines[i][n] < lines[i][n-1]) and (lines[i][n] < lines[i+1][n]):
                    lowlist.append( (i,n) )
            else:
                if(lines[i][n] < lines[i][n-1]) and (lines[i][n] < lines[i][n+1]) and (lines[i][n] < lines[i+1][n]):
                    lowlist.append( (i,n) )               
        #last row:
        elif(i == len(lines)-1):
            #first col
            if(n == 0):
                if(lines[i][n] < lines[i][n+1]) and (lines[i][n] < lines[i-1][n]):
                    lowlist.append( (i,n) )
            #last col
            elif(n == len(line) -1):
                if(lines[i][n] < lines[i][n-1]) and (lines[i][n] < lines[i-1][n]):
                    lowlist.append( (i,n) )
            else:
                if(lines[i][n] < lines[i][n-1]) and (lines[i][n] < lines[i][n+1]) and (lines[i][n] < lines[i-1][n]):
                    lowlist.append( (i,n) )
        #everything else
        else:
            #first col
            if(n == 0):
                if(lines[i][n] < lines[i][n+1]) and (lines[i][n] < lines[i-1][n]) and (lines[i][n] < lines[i+1][n]):
                    lowlist.append( (i,n) )
            #last col
            elif(n == len(line) -1):
                if(lines[i][n] < lines[i][n-1]) and (lines[i][n] < lines[i-1][n]) and (lines[i][n] < lines[i+1][n]):
                    lowlist.append( (i,n) )
            else:
                if(lines[i][n] < lines[i][n-1]) and (lines[i][n] < lines[i][n+1]) and (lines[i][n] < lines[i-1][n]) and (lines[i][n] < lines[i+1][n]):
                    lowlist.append( (i,n) )
            pass

print lowlist
risklevel = 0
for coord in lowlist:
     risklevel += 1 + int(lines[int(coord[0])][int(coord[1])])
print risklevel

#for i in range(len(lowlist)):
#    lowlist[i][0] = int(lowlist[i][0])
#    lowlist[1][1] = int(lowlist[1][1])
#print lowlist

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    

def basincheck(list, coord):
    print "basincheck called with coord", coord
    #row
    if(coord[0] == 0):
        #col
        if(coord[1] == 0):
            #right
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]+1]) and int(lines[coord[0]][coord[1]+1]) < 9:
                list.add((coord[0], coord[1] + 1))
                basincheck(list, (coord[0], coord[1] + 1))
            #down
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]+1][coord[1]]) and int(lines[coord[0]+1][coord[1]]) < 9:
                list.add((coord[0]+1, coord[1]))
                basincheck(list, (coord[0]+1, coord[1]))
        elif(coord[1] == len(lines[0]) - 1):
            #left
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]-1]) and int(lines[coord[0]][coord[1]-1]) < 9:
                list.add((coord[0], coord[1]-1))
                basincheck(list, (coord[0], coord[1]-1))
            #down
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]+1][coord[1]]) and int(lines[coord[0]+1][coord[1]]) < 9:
                list.add((coord[0]+1, coord[1]))
                basincheck(list, (coord[0]+1, coord[1]))
        else:
            print(len(lines[0])), lines[0]
            #right
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]+1]) and int(lines[coord[0]][coord[1]+1]) < 9:
                list.add((coord[0], coord[1]+1))
                basincheck(list, (coord[0], coord[1]+1))
            #left
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]-1]) and int(lines[coord[0]][coord[1]-1]) < 9:
                list.add((coord[0] , coord[1]-1))
                basincheck(list, (coord[0] , coord[1] - 1))
            #down
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]+1][coord[1]]) and int(lines[coord[0]+1][coord[1]]) < 9:
                list.add((coord[0]+1, coord[1]))
                basincheck(list, (coord[0]+1, coord[1]))

    elif(coord[0] == len(lines) - 1):
        #col
        if(coord[1] == 0):
            #right
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]+1]) and int(lines[coord[0]][coord[1]+1]) < 9:
                list.add((coord[0], coord[1] +1))
                basincheck(list, (coord[0], coord[1]+1))
            #up
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]-1][coord[1]]) and int(lines[coord[0]-1][coord[1]]) < 9:
                list.add((coord[0]-1, coord[1]))
                basincheck(list, (coord[0]-1, coord[1]))
        elif(coord[1] == len(lines[0]) - 1):
            #left
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1] -1]) and int(lines[coord[0]][coord[1]-1]) < 9:
                list.add((coord[0], coord[1]-1))
                basincheck(list, (coord[0], coord[1]-1))

            #up
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]-1][coord[1]]) and int(lines[coord[0]-1][coord[1]]) < 9:
                list.add((coord[0]-1, coord[1]))
                basincheck(list, (coord[0]-1, coord[1]))
        else:
            #right
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1] +1]) and int(lines[coord[0]][coord[1]+1]) < 9:
                list.add((coord[0] , coord[1] +1))
                basincheck(list, (coord[0] , coord[1]+1))
            #left
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]-1]) and int(lines[coord[0]][coord[1]-1]) < 9:
                list.add((coord[0], coord[1]-1))
                basincheck(list, (coord[0] , coord[1]-1))
            #up
            if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]-1][coord[1]]) and int(lines[coord[0]-1][coord[1]]) < 9:
                list.add((coord[0]-1, coord[1]))
                basincheck(list, (coord[0]-1, coord[1]))
    else:
            if(coord[1] == 0):
                #down
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0] + 1][coord[1]]) and int(lines[coord[0] + 1][coord[1]]) < 9:
                    list.add((coord[0] + 1, coord[1]))
                    basincheck(list, (coord[0] + 1, coord[1]))
                #up
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0] - 1][coord[1]]) and int(lines[coord[0] - 1][coord[1]]) < 9:
                    list.add((coord[0] - 1, coord[1]))
                    basincheck(list, (coord[0] - 1, coord[1]))
                #right
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]+1]) and int(lines[coord[0]][coord[1]+1]) < 9:
                    list.add((coord[0], coord[1]+1))
                    basincheck(list, (coord[0], coord[1]+1))
            elif(coord[1] == len(lines[0]) - 1):
                #down
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0] + 1][coord[1]]) and int(lines[coord[0] + 1][coord[1]]) < 9:
                    list.add((coord[0] + 1, coord[1]))
                    basincheck(list, (coord[0] + 1, coord[1]))
                #up
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0] - 1][coord[1]]) and int(lines[coord[0] - 1][coord[1]]) < 9:
                    list.add((coord[0] - 1, coord[1]))
                    basincheck(list, (coord[0] - 1, coord[1]))
                #left
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]-1]) and int(lines[coord[0]][coord[1]-1]) < 9:
                    list.add((coord[0], coord[1]-1))
                    basincheck(list, (coord[0], coord[1]-1))
            else:
                #down
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0] + 1][coord[1]]) and int(lines[coord[0] + 1][coord[1]]) < 9:
                    list.add((coord[0] + 1, coord[1]))
                    basincheck(list, (coord[0] + 1, coord[1]))
                #up
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0] - 1][coord[1]]) and int(lines[coord[0] - 1][coord[1]]) < 9:
                    list.add((coord[0] - 1, coord[1]))
                    basincheck(list, (coord[0] - 1, coord[1]))
                #left
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]-1]) and int(lines[coord[0]][coord[1]-1]) < 9:
                    list.add((coord[0], coord[1]-1))
                    basincheck(list, (coord[0], coord[1]-1))
                #right
                if int(lines[coord[0]][coord[1]]) < int(lines[coord[0]][coord[1]+1]) and int(lines[coord[0]][coord[1]+1]) < 9:
                    list.add((coord[0], coord[1]+1))
                    basincheck(list, (coord[0], coord[1]+1))


basinlistoflists = []    
for coord in lowlist:
    basinlist=set()
    basinlist.add(coord)
    basincheck(basinlist, coord)
    basinlistoflists.append(basinlist)

print basinlistoflists

countlist = []
for basinset in basinlistoflists:
    countlist.append(len(basinset))
print countlist
countlist.sort(reverse=True)
print countlist
productof3counts = countlist[0]*countlist[1]*countlist[2]
print productof3counts
    