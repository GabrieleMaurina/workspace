fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
for i in range(cases):
    fout.write("Case #" + (str)(i + 1) + ": ")
    C, F, X = [float(i) for i in fin.readline().split()]

    prod = 2.0
    derivata = -1
    tot_prec = X / prod
    tot = 0
    while derivata <= 0:
        tot += C / prod
        prod += F
        tot += X / prod
        derivata = tot - tot_prec
        if derivata > 0:
           fout.write("%.7f" % tot_prec)
        tot_prec = tot
        tot -= X / prod    
    fout.write("\n")
    
fin.close()
fout.close()
