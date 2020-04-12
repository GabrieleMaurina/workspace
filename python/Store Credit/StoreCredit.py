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

    for e in range(len(items)):
        for o in range(len(items)):
            if o > e and items[e] + items[o] == c:
                fout.write(str(e + 1) + " " + str(o + 1));
                break
        else:
            continue
        break
    
    fout.write("\n")
    
fin.close()
fout.close()

print(millis() - start)
