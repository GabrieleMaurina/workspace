import math

fin = open("input.txt", "r")
fout = open("output.txt", "w")

cases = eval(fin.readline())
for i in range(cases):
    fout.write("Case #" + (str)(i + 1) + ":\n")
    R, C, M = [int(i) for i in fin.readline().split()]

    field = [["*" for i in range(C)] for j in range(R)]

    V = R * C - M
    found = 0
    lato = 0
    
#    if M <= 1:
#        field[0][0] = "c"
#        found = 1
#        lato = 1
       
    if M < 4 and M > 1 :
        fout.write("Impossible\n")
        continue
    
    minor = min(R, C, int(math.sqrt(V))) + 1

    for j in range(2, minor):
        if V % j == 0:
            if V // j <= max(R, C):
                found = 1
                lato = j
                break
        elif V % j > 1:
            if V // j < max(R, C) or j < min(R, C):
                found = 1
                lato = j
                break
    if not(found):
        fout.write("Impossible\n")
        continue
    
    x, y, resto = 0, 0, 0

    if R >= C:
        x = lato
        y = V // lato
    else:
        x = V // lato
        y = lato

    fondo = 0
    
    if V % lato > 0:
        resto = V % lato
        if y - 1 < R:
            fondo = 1

    if fondo == 1:
            for e in range (y):
                for f in range (x):
                    field[e][f] = "."
            for f in range (resto):
                field[y][f] = "."
    if fondo == 0:
            for e in range (resto):
                for f in range (x + 1):
                    field[e][f] = "."
            for e in range (resto + 1, y):
                for f in range (x):
                    field[e][f] = "."
    
    for i in range(R):
        for j in range(C):
            fout.write(field[i][j])
        fout.write("\n")
    
    fout.write("\n")
    
fin.close()
fout.close()
