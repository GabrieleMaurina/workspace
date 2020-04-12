fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

def printMat(mat):
    for y in range(len(mat[0])):
        line = ""
        for x in range(len(mat)):
            line += str(mat[x][y]) + " "
        print(line)

def printMat1(mat):
    global fout
    for y in range(len(mat[0])):
        for x in range(len(mat)):
            fout.write(str(mat[x][y]))
        fout.write("\n")

tot = 0
found = False

def evaluate(mat, y, B, M, b):
    global tot
    
    if tot == -1:
        return

    
    if y in b:
        tot = -1
        return
    #print("Y: " + str(y))
    b.append(y)
    if y == B - 1:
        tot += 1
        if tot > M:
            tot = -1
        b.remove(y)
        return
    for i in range(B):
        if mat[i][y] == 1:
            evaluate(mat, i, B, M, b)
    b.remove(y)

def okHo(mat, B):
    for i in range(B):
        if mat[i][0] == 1:
            return True
    return False

def okVe(mat, B):
    for i in range(B):
        if mat[B - 1][i] == 1:
            return True
    return False

def compute(mat, x, y, B, M):
    global tot
    global found
    if found:
        return

    if y == B:
        if okVe(mat, B):
            tot = 0
            #printMat(mat)
            evaluate(mat, 0, B, M, [])
            if tot == M:
                found = True
            #print("TOT: " + str(tot))
            #input()
        return

    if y == 1 and not okHo(mat, B):
        return
    
    nextX = 0
    nextY = y + 1
    if x < B - 1:
        nextX = x + 1
        nextY = y

    compute(mat, nextX, nextY, B, M)

    if found:
        return
    
    if x != y  and x > 0 and mat[y][x] == 0:
        mat[x][y] = 1
        compute(mat, nextX, nextY, B, M)
        if found:
            return
        mat[x][y] = 0

print("CASES: " + str(cases))

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    
    B, M = [int(x) for x in fin.readline().split()]
    print(str(i + 1) + "   B: " + str(B) + " M: " + str(M))
    mat = [[0 for x in range(B)] for y in range(B)]

    for i in range(B):
        mat[i][i] = 0
        mat[i][B - 1] = 0

    found = False
    compute(mat, 0, 0, B, M)

    if found:
        #print("FOUND")
        fout.write("POSSIBLE\n")
        #printMat(mat)
        printMat1(mat)
    else:
        fout.write("IMPOSSIBLE\n")
    
fin.close()
fout.close()
