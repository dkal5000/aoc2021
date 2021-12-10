import numpy
infile = open("day10input.txt", "r")
lines = infile.readlines()
pairs =  [( ")","(" ), ("]","["), (">","<"), ("}", "{") ]
pairs = dict(pairs)
openers = ["[","{","<","("]
closers = ["]","}",">",")"]
stacklevel = 0

score = [(")", 3), ("]", 57),("}", 1197), (">",25137)]
score = dict(score)
scorecount = [(")", 0), ("]", 0),("}", 0), (">",0)]
scorecount = dict(scorecount)

unmatchedscore = [("(", 1), ("[", 2),("{", 3), ("<",4)]
unmatchedscore = dict(unmatchedscore)
unmatchedvalue = [("(", 0), ("[", 0),("{", 0), ("<",0)]
unmatchedvalue = dict(unmatchedvalue)

scorelist = []
unmatchedlist = []

for j in range(len(lines)):
    earlyTerm = 0
    expectedMatchList = []
    for i in range(len(lines[j].strip())):
        #print expectedMatchList
        if openers.count(lines[j][i]):
            expectedMatchList.append(lines[j][i])
        else:
            if pairs[lines[j][i]] == expectedMatchList.pop():
                #print("Match Found") 
                pass
            else:
                print("Early Termination")
                scorecount[lines[j][i]] += 1
                earlyTerm = 1

    if(len(expectedMatchList)) !=0 and earlyTerm == 0:
            print("Unmatched start symbols")
            print expectedMatchList
            k = 0
            totalscore2 = 0
            for _ in range(len(expectedMatchList)):
                symbol = expectedMatchList.pop()
                totalscore2= 5*totalscore2 + unmatchedscore[symbol]
            scorelist.append(totalscore2)
           
            
                
totalscore = 0
print scorecount
for n in closers:
    totalscore += scorecount[n]*score[n]
print totalscore

print scorelist
scorelist.sort()
print scorelist
print scorelist[len(scorelist)/2]

def findMatchingPairs(line, startPos, charToMatch):
    global stacklevel
    currentStack = stacklevel
    retVal = 0
    charToMatchNext = "*"
    print "Stack Level ", stacklevel
    char = lines[line][startPos]
    print "Processing ", char
    #print expectedMatchList
    if char != charToMatch:
        if char == "[":
            charToMatchNext = "]"
        elif char == "]":
            print "Expected ",charToMatch, " but found ", char, "instead"    
        elif char == "(":
            charToMatchNext = ")"
        elif char == ")":
            print "Expected ",charToMatch, " but found ", char, "instead"
        elif char == "{":
            charToMatchNext = "}"
        elif char == "}":
            print "Expected ",charToMatch, " but found ", char, "instead"
        elif char == "<":
            charToMatchNext = ">"
        elif char == ">":
            print "Expected ",charToMatch, " but found ", char, "instead"
        elif char == "*":
            print "First"
        elif char == "\r":
            print "Reached end of line"
        else:
            print "Unknown char"

        if(charToMatchNext != "*"):
            print "looking for ", charToMatchNext
            stacklevel += 1 
            print("Not A Match")
            retVal = findMatchingPairs(line, startPos + 1, charToMatchNext)
            stacklevel -= 1
            print "Current Stack ", currentStack
            print charToMatch
                       
    else:         
        print "*** Found match for ", charToMatch
        retVal = 1
    
    i = 0
    while retVal == 1:
        retVal = findMatchingPairs(line, startPos + 1 + i, charToMatch)
        i += 1        

    print "Return value", retVal
    return retVal
        
        


#findMatchingPairs(0, 0, "*")
#for i in range(len(lines[0].strip())):
#    findMatchingPairs(i, "*")
