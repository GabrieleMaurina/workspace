fin = open("A-large.in", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
for e in range(cases):
    fout.write("Case #" + (str)(e + 1) + ": ")
    N, S = [o for o in fin.readline().split()]
    t = 0
    f = 0
    p = 0
    i = 0
    for s in S:
        s = int(s)
        
        if p == 1 and s != 0:
            if t < i:
                f1 = i - t
                f += f1
                t += f1
        
        if s == 0:
            p = 1
        else:
            p = 0
        i += 1
        t += s

    fout.write(str(f))
        
    fout.write("\n")
    
fin.close()
fout.close()
