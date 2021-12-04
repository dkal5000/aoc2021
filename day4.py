import numpy
infile = open("input_day4a.txt", "r")
lines = infile.readlines()
lineslen = len(lines)
#print lines
#print lineslen
bingocall = lines[0].rstrip("\r\n").split(",")
#print bingocall
lines = lines[1:lineslen]
bingocards = []
bingocard = []
hitmaps = []
hitmap = []
i = 0
winners = []

def sumNumsNotHit(card):
    totalNotHit = 0
    for y in range(5):
        for x in range(5):
           if(hitmaps[card][x][y] == 0):
               totalNotHit = totalNotHit + int(bingocards[card][x][y])
    return totalNotHit
            

def checkBingo():
    for card in range(len(bingocards)):
        if card in winners:
            continue

        for y in range(5):
            hittotalhor = 0
            wintotalhor = 0
            for x in range(5):
                hittotalhor = hittotalhor +  hitmaps[card][x][y]
                wintotalhor = wintotalhor + int(bingocards[card][x][y])
                if hittotalhor == 5:
                    print "BINGO HORIZONTAL"
                    winners.append(card)
                    return
        for x in range(5):
            hittotalvert = 0
            wintotalvert = 0
            for y in range(5):
                hittotalvert = hittotalvert +  hitmaps[card][x][y]
                wintotalvert = wintotalvert + int(bingocards[card][x][y])
                if hittotalvert == 5:
                    print "BINGO VERTICAL"
                    winners.append(card)
                    return

    #return (-1,0)

def callBingoGame():
    for callnum in bingocall:
        for card in range(len(bingocards)):
            for y in range(5):
                for x in range(5):             
                    if bingocards[card][x][y] == callnum:
                        print "HIT"
                        print callnum
                        print card
                        print x
                        print y
                        hitmaps[card][x][y] = 1
                        checkBingo()
                        if len(winners) == len(bingocards):
                            print "LAST CARD HAS BINGO"
                            return(card, callnum)
                        #if(wincard[1] > 0):
                            #print "BINGO"
                            #print "Card"
                            #print wincard[0]
                            #print "SUM"
                            #print wincard[1]
                            
                            #return (wincard[0],callnum)
                            


#print lines

for line in lines:
    if line == "\r\n":
        continue
    bingocard.append(line.split())
    hitmap.append([0,0,0,0,0])
    i = i + 1
    if(i == 5):
        bingocards.append(bingocard)
        hitmaps.append(hitmap)
        bingocard = []
        hitmap = []
        i = 0

print bingocards

winningcard = callBingoGame()

sum = sumNumsNotHit(winningcard[0])
print sum

#print "Last Winning Card"
print winningcard
print "Sum of not called numbers"
print sum
print "Last Called Number"
print winningcard[1]
print "ANSWER"
print sum*int(winningcard[1])
#print "****************"
print "Winning Card"
print bingocards[winningcard[0]]
#print winners