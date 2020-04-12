fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    S = fin.readline().replace("\n", "")
    y = ""
    
    for e in range(len(S)):
        if e == 0:
            y = S[e]
        else:
            tmp = sorted([S[e], y[0]], reverse = True)
            if tmp[0] == S[e]:
                y = S[e] + y
            else:
                y = y + S[e]

    fout.write(y)
    
    fout.write("\n")
    
fin.close()
fout.close()
