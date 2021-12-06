import numpy
infile = open("day6input.txt", "r")
line = infile.readline()
line = line.split(",")
for val in range(len(line)):
    line[val] = int(line[val])
print "Input Vals", line
total = 0
print line[0]
for num in range(len(line)):
    days = [0,0,0,0,0,0,0,0,0]
    days[line[num]] = 1
    for day in range(256):
        print day
        print days
        popped = days.pop(0)
        days.append(popped)
        days[6]+=popped
        
    for val in days:
        total += val
print total

       