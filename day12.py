def find_items_in_list(list, item):
    foundlist = []
    for x in list:
        if(x[0] == item):
            foundlist.append(x)
    return foundlist


def read_file(name):
    list = []
    file = open(name)
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(",")
        for element in line:
            element = element.split("-")
            list.append((element[0], element[1]))
    return list

#def followLink():
    
        

mylist = read_file("day12testinput.txt")
print mylist

for item in mylist:
    print find_items_in_list(mylist, item[0])
 
       
        

