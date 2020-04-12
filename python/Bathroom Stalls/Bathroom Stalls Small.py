from math import *

fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    print(i / cases * 100)
    fout.write("Case #" + str(i + 1) + ": ")
    N, K = [int(x) for x in fin.readline().split()]
    
    s = [N]

    maxS = 0
    minS = 0
    for i in range(K):
        n = max(s)
        s.remove(n)
        n -= 1
        n /= 2
        minN = floor(n)
        maxN = ceil(n)

        if minN > 0:
            s.append(minN)
        if maxN > 0:
            s.append(maxN)
        
        if i == K - 1:
            fout.write(str(max(minN, maxN)) + " " + str(min(minN, maxN)))
    
    fout.write("\n")
    
fin.close()
fout.close()
