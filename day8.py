import numpy
grandtotalnumber = 0
positiona  = [0, 2, 3, 5, 6, 7, 8, 9]
positionb = [0, 4, 5, 6, 8, 9]
positionc = [0, 1, 2, 3, 4, 7, 8, 9]
positiond = [2, 3, 4, 5, 6, 8, 9]
positione = [0, 2, 6, 8]
positionf = [0, 1, 3, 4, 5, 6, 7, 8, 9]
positiong = [0, 2, 3, 5, 6, 8, 9]

positionlist = [positiona, positionb, positionc, positiond, positione, positionf, positiong]

num0 = 6
num1 = 2 #unique
num2 = 5
num3 = 5
num4 = 4 #unique
num5 = 5
num6 = 6
num7 = 3 #unique
num8 = 7 #unique
num9 = 6

numlist = [num1, num4, num7, num8, num2, num3, num5, num0, num6, num9]

##################################################INPUT
infile = open("day8input.txt", "r")
lines = infile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split("|")
    lines[i][0] = lines[i][0].split()
    lines[i][1] = lines[i][1].split()
    print lines[i]
####################################################LOOP
for k in range(len(lines)):
    numberofones = 0
    numberoffours = 0
    numberofsevens = 0
    numberofeights = 0
    for i in range(len(lines)):
        for entry in lines[i][1]:
            if(len(entry) == num1):
               numberofones+=1
            elif(len(entry) == num4):
               numberoffours+=1
            elif(len(entry) == num7):
               numberofsevens +=1
            elif(len(entry) == num8):
               numberofeights +=1
            else:
                pass

    print numberofones+numberoffours+numberofsevens+numberofeights
    ############################################################################## END OF PART 1
    lettersfor1 = []
    countfor1 = [0,0]
    lettersfor4 = []
    lettersfor7 = []
    lettersfor8 = []
    #################################################################### MAKE LIST OF LETTERS FOR KNOWN NUMBERS
    for entry in lines[k][0]:
        if(len(entry) == num1):
            for j in range(num1):
                lettersfor1.append(entry[j])
            print "1", lettersfor1
        elif(len(entry) == num4):
            for j in range(num4):
                lettersfor4.append(entry[j])
            print "4", lettersfor4
        elif(len(entry) == num7):
            for j in range(num7):
                lettersfor7.append(entry[j])
            print "7", lettersfor7
        elif(len(entry) == num8):
            for j in range(num8):
                lettersfor8.append(entry[j])
            print "8", lettersfor8
        else:
            pass

    correspondstof = ""
    correspondstoc = ""
    # f is only missing in 2 (size 5), there are 3 size 5
    # c is only missing in 5 and 6 (size 5 and 6)
    counter = 0
    for letter in lettersfor1:    
        for entry in lines[k][0]:
            if(len(entry)) == 2:
                continue
            if(entry.find(letter))==-1:
                countfor1[counter] += 1
        counter +=1
    
    print[countfor1]
####################################FIND POSITIONS OF LETTERS IN 1
    counter = 0
    for num in countfor1:
        if(num == 1): #Only one missing F is 2       
            correspondstof = lettersfor1[counter]
        else:
            correspondstoc = lettersfor1[counter] 
        counter += 1

    print correspondstoc ,"corresponds to c"
    print correspondstof ,"corresponds to f"
###################################FIND POSITIONS OF LETTERS IN 7

    lettersfor7.remove(correspondstoc)
    lettersfor7.remove(correspondstof)
    correspondstoa = lettersfor7.pop()

    print correspondstoa ,"corresponds to a"
###################################FIND POSITIONS OF LETTERS IN 4
    counter = 0
    lettersfor4.remove(correspondstoc)
    lettersfor4.remove(correspondstof)
#    lettersfor4.remove(correspondstoa) # there is no A here
    #2 has d but not b and size 5
    #3 has d and not b and size 5
    #0 is the only one that has b but not d and size 6
    #will have two letters left
    counter = 0
    for letter in lettersfor4:
        for entry in lines[k][0]:
            #length of 6
            if(len(entry)) == 6:
               #did not find the letter, so this is 0
                 if(entry.find(letter))==-1:
                     correspondstod = letter
                     lettersfor4.remove(letter)
                     correspondstob = lettersfor4.pop()
                     break

    print correspondstod ,"corresponds to d"
    print correspondstob ,"corresponds to b"

    lettersfor8.remove(correspondstoc)
    lettersfor8.remove(correspondstof)
    lettersfor8.remove(correspondstoa)
    lettersfor8.remove(correspondstob)
    lettersfor8.remove(correspondstod)


    #only e and g remain
    #5 has g but not e and is size 5
    #3 has g but not e and is size 5
    #9 has g but not e and is size 6 
    for letter in lettersfor8:
        for entry in lines[k][0]:
            #length of 6
            if(len(entry)) == 6:
               #did not find the letter, so this is 9
                 if(entry.find(letter))==-1:
                     correspondstoe = letter
                     lettersfor8.remove(letter)
                     correspondstog = lettersfor8.pop()
                     break
    print correspondstog ,"corresponds to g"
    print correspondstoe ,"corresponds to e"
    multiplier = 1000
    currentnumber = 0
    totalnumber = 0
    for entry in lines[k][1]:
        print entry
        if(len(entry) == 2):
            print "Number 1"
            currentnumber = 1
        elif(len(entry) == 4):
            print "Number 4"
            currentnumber = 4
        elif(len(entry) == 3):
            print "Number 7"
            currentnumber = 7
        elif(len(entry) == 7):
            print "Number 8"
            currentnumber = 8
        elif(len(entry) == 5):
            if entry.find(correspondstoa) > -1 and entry.find(correspondstoc) > -1 and entry.find(correspondstod) > -1 and entry.find(correspondstoe) > -1 and entry.find(correspondstog) > -1:
                print "Number 2"
                currentnumber = 2
            elif entry.find(correspondstoa) > -1 and entry.find(correspondstoc) > -1 and entry.find(correspondstod) > -1 and entry.find(correspondstof) > -1 and entry.find(correspondstog) > -1:
                print "Number 3"
                currentnumber = 3
            elif entry.find(correspondstoa) > -1 and entry.find(correspondstob) > -1 and entry.find(correspondstod) > -1 and entry.find(correspondstof) > -1 and entry.find(correspondstog) > -1:
                print "Number 5"
                currentnumber = 5
            else:
                print "UNKNOWN COMBO!!"
        else:
            if(entry.find(correspondstoa) > -1) and (entry.find(correspondstob) > -1) and (entry.find(correspondstoc) > -1) and (entry.find(correspondstoe) > -1) and (entry.find(correspondstof) > -1) and (entry.find(correspondstog) > -1):
                print "Number 0"
                currentnumber = 0
            elif (entry.find(correspondstoa) > -1) and (entry.find(correspondstob) > -1) and (entry.find(correspondstod) > -1) and (entry.find(correspondstoe) > -1) and (entry.find(correspondstof) > -1) and (entry.find(correspondstog) > -1):
                print "Number 6"
                currentnumber = 6
            elif (entry.find(correspondstoa) > -1) and (entry.find(correspondstob) > -1) and (entry.find(correspondstoc) > -1) and (entry.find(correspondstod) > -1) and (entry.find(correspondstof) > -1) and (entry.find(correspondstog) > -1):
                print "Number 9"
                currentnumber = 9
            else:
                print "UNKNOWN COMBO2!!"
        totalnumber += currentnumber *  multiplier
        multiplier /= 10

    print totalnumber
    grandtotalnumber+=totalnumber
print grandtotalnumber   