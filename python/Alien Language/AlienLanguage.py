SMALL = "A-small.in"
LARGE = "A-large.in"

fin = open(SMALL, "r")
fout = open("output.out", "w")

L, D, N = [int(x) for x in fin.readline().split()]
dictionary = []

for i in range(D):
    dictionary.append(fin.readline())

for i in range(N):
    fout.write("Case #" + str(i + 1) + ": ")

    line = fin.readline()
    if line[-1] == "\n":
        line = line[:-1]
    brackets = False
    word = [[]]
    index = 0

    for c in line:
        if c == "(":
            brackets = True
        elif c == ")":
            brackets = False
            index += 1
            word.append([])
        elif brackets == True:
            word[index].append(c)
        elif brackets == False:
            word[index].append(c)
            index += 1
            word.append([])
    word.pop()

    print(word)
    
    fout.write("\n")
    
fin.close()
fout.close()
