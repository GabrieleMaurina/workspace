SMALL = "A-small.in"
LARGE = "A-large.in"

def scalarProduct(v1, v2):
    res = 0
    for x in range(len(v1)):
        res += v1[x] * v2[x]
    return res

fin = open(SMALL, "r")
fout = open("output.out", "w")

cases = eval(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    fin.readline()
    v1 = [eval(x) for x in fin.readline().split()]
    v2 = [eval(x) for x in fin.readline().split()]
    fout.write(str(scalarProduct(sorted(v1), sorted(v2, reverse=True))))
    fout.write("\n")
    
fin.close()
fout.close()
