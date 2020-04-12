SMALL = "A-small.in"
LARGE = "A-large.in"

def findItems(items, c):
    for i0, item0 in enumerate(items):
        for i1, item1 in enumerate(items):
            if item0 + item1 == c and i0 != i1:
                return [i0, i1]
    return []

fin = open(SMALL, "r")
fout = open("output.out", "w")
cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    c = int(fin.readline())
    fin.readline()
    items = [int(item) for item in fin.readline().split()]
    items = findItems(items, c)
    fout.write(str(items[0] + 1) + " " + str(items[1] + 1))
    fout.write("\n")
    
fin.close()
fout.close()
