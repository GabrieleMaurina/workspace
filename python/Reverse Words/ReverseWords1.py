SMALL = "B-small.in"
LARGE = "B-large.in"

fin = open(SMALL, "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    words = fin.readline().split()
    for word in reversed(words):
        fout.write(word + " ")
    fout.write("\n")
    
fin.close()
fout.close()
