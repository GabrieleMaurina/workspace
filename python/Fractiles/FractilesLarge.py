import math

SMALL = "A-small.in"
LARGE = "A-large.in"

fin = open(SMALL, "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    k, c, s = [int(e) for e in fin.readline().split()]
    if s < k / c:
        fout.write("IMPOSSIBLE")
    else:
        pos = []
        index = 0
        while index < k:
            p = 0
            for counter in range(c):
                delta = 1
                if index + c - counter > k:
                    delta = 1 + index + c - counter - k
                p += (index + c - counter - delta) * int(math.pow(k, counter))
            index += c
            pos.append(p)

        for p in pos:
            fout.write(str(p + 1) + " ")
    
    fout.write("\n")
    
fin.close()
fout.close()
