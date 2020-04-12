SMALL = "A-small.in"
LARGE = "A-large.in"

fin = open(SMALL, "r")
fout = open("output.out", "w")

cases = int(fin.readline())

def flip(pancakes):
    temp = []
    for p in pancakes:
        temp.append(not p)
    return list(reversed(temp))

def doFlip(pancakes, i):
    temp = flip(pancakes[:i])
    temp.extend(pancakes[i:])
    return temp

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    pancakes = []
    
    for p in fin.readline():
        if p == '+':
            pancakes.append(True)
        elif p == '-':
            pancakes.append(False)

    flips = 0
    for e in range(len(pancakes)):
        if e == len(pancakes) - 1:
            if not pancakes[e]:
                pancakes = doFlip(pancakes, e + 1)
                flips += 1
        else:
            if pancakes[e] != pancakes[e + 1]:
                pancakes = doFlip(pancakes, e + 1)
                flips += 1

    fout.write(str(flips))
    
    fout.write("\n")
    
fin.close()
fout.close()
