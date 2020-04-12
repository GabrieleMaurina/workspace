fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    N = int(fin.readline())

    lines = []
    for e in range(2 * N - 1):
        lines.append([int(x) for x in fin.readline().split()])
  
    mat = [[0 for e in range(N)] for o in range(N)]

    UULines = list(lines)

    missing = -1
    missingDir = True
    
    for e in range(N):
        UULines = sorted(UULines)
        first = UULines[0]
        UULines.pop(0)
        pair = None
        for o in range(len(UULines)):
            if first[e] == UULines[o][e]:
                pair = UULines[o]
                UULines.pop(o)
                break
            
        if pair != None:
            firstOkH = True
            pairOkV = True
            for o in range(e):
                if mat[o][e] != first[o]:
                    firstOkH = False
                if mat[e][o] != pair[o]:
                    pairOkV = False
            if firstOkH and pairOkV:
                for o in range(N):
                    mat[o][e] = first[o]
                    mat[e][o] = pair[o]
            else:
                for o in range(N):
                    mat[e][o] = first[o]
                    mat[o][e] = pair[o]

        else:
            missing = e
            firstOkH = True
            for o in range(e):
                if mat[o][e] != first[o]:
                    firstOkH = False
                    break

            if firstOkH:
                for o in range(N):
                    mat[o][e] = first[o]
            else:
                missingDir = False
                for o in range(N):
                    mat[e][o] = first[o]

    '''for e in range(N):
        for o in range(N):
            print(str(mat[o][e]) + " ", end = "")
        print()
    print()
    print()'''


    if missingDir:
        for o in range(N):
            fout.write(str(mat[e][o]) + " ")
    else:
        for o in range(N):
            fout.write(str(mat[o][e]) + " ")
    
    fout.write("\n")
    
fin.close()
fout.close()
