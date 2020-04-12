fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    
    p, K = fin.readline().split()
    p = [x == "+" for x in p]
    K = int(K)
    f = 0
    impossible = False
    
    for i in range(len(p)):
        if not p[i]:
            if i + K <= len(p):
                f += 1
                for j in range(K):
                    p[i + j] = not p[i + j]
            else:
                impossible = True
                break

    if impossible:
        fout.write("IMPOSSIBLE")
    else:
        fout.write(str(f))
    
    fout.write("\n")
    
fin.close()
fout.close()
