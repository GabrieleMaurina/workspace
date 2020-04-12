SMALL = "A-small.in"
LARGE = "A-large.in"

fin = open(SMALL, "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    k, c, s = [int(e) for e in fin.readline().split()]

    if c == 1 or k == 1:
        fout.write("1 ")
    for e in range(k - 1):
        fout.write(str(e + 2) + " ")
    
    fout.write("\n")
    
fin.close()
fout.close()
