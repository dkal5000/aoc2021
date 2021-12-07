import numpy
infile = open("day7input.txt", "r")
line = infile.readline()
line = line.split(",")
max = 0
min = 9999999999
for val in range(len(line)):
    line[val] = int(line[val])
    if line[val] > max:
        max = line[val]
    if line[val] < min:
        min = line[val]
print line
print max
print min
besttotalfuel = 999999999999999
numforbesttotalfuel = -1
for num in range(max - min):
    print num, "*********"
    totalfuel = 0
    for val in line:
    #    print val, num
    #    print "Difference",abs(val - num)
        totalfuel += (abs(val - num)*(abs(val - num) + 1))/2
    if(totalfuel < besttotalfuel):
        besttotalfuel = totalfuel
        numforbesttotalfuel = num
    #print "Total Fuel",totalfuel  
print "BEST", numforbesttotalfuel, besttotalfuel
