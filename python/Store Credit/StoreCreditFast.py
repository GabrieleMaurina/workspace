SMALL = "A-small-practice.in"
LARGE = "A-large-practice.in"

import time

def millis():
    return int(round(time.time() * 1000))

start = millis()

fin = open(LARGE, "r")
fout = open("output.out", "w")
cases = eval(fin.readline())
for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    
    c = eval(fin.readline())
    fin.readline()
    items = [eval(i) for i in fin.readline().split()]
    itemsDict = {}
    for e in range(len(items)):
        if items[e] in itemsDict:
            itemsDict[items[e]].append(e)
        else:
            itemsDict[items[e]] = [e]

    for e in items:
        mate = c - e
        if mate == e:
            if len(itemsDict[mate]) >= 2:
                fout.write(str(itemsDict[mate][0] + 1) + " " + str(itemsDict[mate][1] + 1))
                break
        else:
            if mate in itemsDict:
                fout.write(str(itemsDict[e][0] + 1) + " " + str(itemsDict[mate][0] + 1))
                break
    
    fout.write("\n")
    
fin.close()
fout.close()

print(millis() - start)
