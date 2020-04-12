SMALL = "B-small-practice.in"
LARGE = "B-large-practice.in"
OUTPUT = "output.out"

fin = open(LARGE, "r")
fout = open(OUTPUT, "w")

cases = eval(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": " + " ".join(reversed(fin.readline().split())) + "\n")
    
fin.close()
fout.close()
