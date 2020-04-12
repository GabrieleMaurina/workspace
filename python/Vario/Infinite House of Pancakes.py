SMALL = "B-small-attempt3.in"
LARGE = "B-large.in"
fin = open("C:\\Users\\Gabriele\\Downloads\\" + SMALL, "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
for e in range(cases):
    fout.write("Case #" + (str)(e + 1) + ": ")
    fin.readline()
    line = fin.readline().split()
    B = 10

    
    
    fout.write("\n")
    
fin.close()
fout.close()
