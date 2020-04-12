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
    FW = 0
    
    while strs[0] != "":
        c = strs[0][0]
        a = strs[0].count(c);
        b = strs[1].count(c);
        #print(c)
        #print(str(a))
        #print(str(b))
        
        if a == b:
            pass
        elif a > 1 or b > 1:
            tot += abs(a - b)
        else:
            fout.write("Fegla Won");
            FW = 1
            break
        strs[0] = strs[0].replace(c, "")
        strs[1] = strs[1].replace(c, "")
        #print(strs[0])
        #print(strs[1])
        #print()

    if strs[0] == "" and strs[1] == "":
        fout.write(str(tot))
    
    fout.write("\n")
    
fin.close()
fout.close()
