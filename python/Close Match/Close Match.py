fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    n1, n2 = [list(x) for x in fin.readline().split()]

    equals = -1
    for e in range(len(n1)):
        if n1[e] != "?" and n2[e] != "?" and n1[e] != n2[e]:
            equals = e
    if equals == -1:
         for e in range(len(n1)):
            if n1[e] == "?" and n2[e] == "?":
                n1[e] = "0"
                n2[e] = "0"
            elif n1[e] == "?":
                n1[e] = n2[e]
            elif n2[e] == "?":
                n2[e] = n1[e]
    else:
        for e in range(equals):
            if n1[e] == "?" and n2[e] == "?":
                n1[e] = "0"
                n2[e] = "0"
            elif n1[e] == "?":
                n1[e] = n2[e]
            elif n2[e] == "?":
                n2[e] = n1[e]
        N1 = int("".join(n1[:equals + 1]))
        N2 = int("".join(n2[:equals + 1]))

        if N1 > N2:
            for e in range(len(n1)):
                if n1[e] == "?":
                    n1[e] = "0"
                if n2[e] == "?":
                    n2[e] = "9"
        else:
            for e in range(len(n1)):
                if n1[e] == "?":
                    n1[e] = "9"
                if n2[e] == "?":
                    n2[e] = "0"

    fout.write("".join(n1) + " " + "".join(n2))
    
    fout.write("\n")
    
fin.close()
fout.close()
