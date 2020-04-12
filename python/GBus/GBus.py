fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ":")
    N = int(fin.readline())
    b = [int(x) for x in fin.readline().split()]
    
    c = [0] * 5000
    
    for j in range(N):
        for k in range(b[j * 2], b[j * 2 + 1] + 1):
            c[k - 1] += 1
    
    P = int(fin.readline())
    for j in range(P):
        t = int(fin.readline()) - 1
        fout.write(" " + str(c[t]))
    
    fin.readline()
    fout.write("\n")
    
fin.close()
fout.close()