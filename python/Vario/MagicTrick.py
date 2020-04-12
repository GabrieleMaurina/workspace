fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
for i in range(cases):
    fout.write("Case #" + (str)(i + 1)+ ": ")
    mat1 = [ [ 0 for j in range(4) ] for k in range(4) ]
    mat2 = [ [ 0 for j in range(4) ] for k in range(4) ]
    line1 = eval(fin.readline()) - 1
    for j in range(4):
         mat1[j] = fin.readline().split()
    line2 = eval(fin.readline()) - 1
    for j in range(4):
         mat2[j] = fin.readline().split()
    comune = len(set(mat1[line1]).intersection(mat2[line2]))
    #print(mat1[line1])
    #print(mat2[line2])
    if comune == 1:
        fout.write(str(list(set(mat1[line1]).intersection(mat2[line2]))[0]))
    elif comune > 1:
        fout.write("Bad magician!")
    else:
        fout.write("Volunteer cheated!")
    fout.write("\n")
    
fin.close()
fout.close()
