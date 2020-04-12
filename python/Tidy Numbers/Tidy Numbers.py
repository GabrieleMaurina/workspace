fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    
    n = [int(x) for x in fin.readline().replace("\n", "")]
    for j in range(len(n)):
        found = False
        for i in range(1, len(n)):
            if found:
                n[i] = 9
            else:
                if n[i] < n[i-1]:
                    n[i-1] -= 1
                    n[i] = 9
                    found = True
                else:
                    last = n[i]

    if n[0] == 0:
        n = n[1:]

    for i in range(len(n)):
        fout.write(str(n[i]))
    fout.write("\n")

fin.close()
fout.close()
