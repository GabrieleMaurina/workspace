from math import *

fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    N, K = [int(x) for x in fin.readline().split()]

    r = N / pow(2, floor(log2(K)) + 1) - 1
    r0 = pow(2, floor(log2(K)) + 1)
    r1 = pow(2, floor(log2(K)))
    print(ceil(r), floor(r), r)
    
    fout.write("\n")
    
fin.close()
fout.close()
