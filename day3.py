#returns the bigger list first, smaller list second
def create_list_by_bit_position(bit_position, workinglist, greater):
    list0 = [] #empty
    list1 = [] #empty
    print "Bit Position"
    print bit_position
    for num in workinglist:
        
        if(num & (1 << bit_position)):
            list1.append(num) #add numbers with a 1 at bit position to the 1 list
        else:
            list0.append(num) #add numbers with a 0 at bit position to the 0 list
    print "list1 size"
    print len(list1)
    print "list0 size"
    print len(list0)
    if(greater):
        if( len(list1) >= len(list0)):
            print "returning list 1"
            print list1
            return list1
        else:
            print "returning list 0"
            print list0
            return list0

    else:
        if( len(list0) <= len(list1)):
            print "returning list 0"
            print list0
            return list0
        else:
            print "returning list 1"
            print list1
            return list1

 

infile = open("input.txt", "r")
lines = infile.readlines()
bin_nums = []
max_len = 0
for line in lines:
    my_line = line.rstrip("\r\n")
    if len(my_line) > max_len:
        max_len = len(my_line)
    bin_nums.append(int(my_line,2))
sums = []
for item in range(max_len):
   sums.append(0)

for num in bin_nums:
    for i in range(max_len):
        sums[i] += (num & 1<<i)>>i

print "Max String Length is"
print max_len
print "Num Entries is"
entries = len(bin_nums)
print entries
print sums    

value = 0
notvalue = 0
for x in range(max_len):
        print x 
        print entries-sums[x]
        if( (entries-sums[x]) > sums[x]):
            value += 1 << x
        else:
            notvalue += 1 << x
print "Final Results"
print value
print notvalue
print value * notvalue


print "*****************PART2******************"
print bin_nums
print "GREATER"
mylist = bin_nums
for x in range(max_len):
    mylist = create_list_by_bit_position(max_len - 1 - x, mylist, 1)
    if(len(mylist) == 1):
        break
finalVal1 = mylist.pop()

print "LESS"
mylist = bin_nums
for x in range(max_len):
    mylist = create_list_by_bit_position(max_len- 1 - x, mylist, 0)
    if(len(mylist) == 1):
        break

finalVal2 = mylist.pop()
print finalVal1
print finalVal2
print finalVal1 * finalVal2




        