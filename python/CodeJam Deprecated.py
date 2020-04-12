fin = open('input.in', 'r')
fout = open('output.out', 'w')

cases = int(fin.readline())

for i in range(cases):
    fout.write('Case #' + str(i + 1) + ": ")
    
    fout.write('\n')
    
fin.close()
fout.close()