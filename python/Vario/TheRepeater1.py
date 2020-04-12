fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
for i in range(cases):
    fout.write("Case #" + (str)(i + 1) + ": ")
    
    n = int(fin.readline())
    tot = 0
    strs = []
    strs.append(fin.readline());
    strs.append(fin.readline());
    strs[0] = strs[0][:-1]
    strs[1] = strs[1][:-1]
    c0 = []
    n0 = []
    i0 = 0
    c1 = []
    n1 = []
    i1 = 0
    
    for c in strs[0]:
        if i0 > 0 and c == c0[i0 - 1]:
            n0[i0 - 1] += 1
        else:
            c0.append(c)
            n0.append(1)
            i0 += 1

    for c in strs[1]:
        if i1 > 0 and c == c1[i1 - 1]:
            n1[i1 - 1] += 1
        else:
            c1.append(c)
            n1.append(1)
            i1 += 1

    FW = 0
    i0 = 0
    i1 = 0
    while c0:
        a = n0[i0]
        if i1 >= len(n1):
            fout.write("Fegla Won")
            FW = 1
            break
        b = n1[i1]

        if(c0[i0] != c1[i1]):
            i1 += 1
            fout.write("Fegla Won")
            FW = 1
            break
        
        if a == b:
            pass
        elif a > 1 or b > 1:
            tot += abs(a - b)
        else:
            fout.write("Fegla Won")
            FW = 1
            break

        n0.pop(i0)
        n1.pop(i1)
        c0.pop(i0)
        c1.pop(i1)

    if (not c0) and (not c1):
        fout.write(str(tot))
    elif FW == 0:
        fout.write("Fegla Won")
    
    fout.write("\n")
    
fin.close()
fout.close()
