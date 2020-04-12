fin = open('input.in', 'r')
fout = open('output.out', 'w')

cases = int(fin.readline())

for i in range(cases):
    fout.write('Case #' + str(i + 1) + ":\n")
    
    N, Q = [int(x) for x in fin.readline().split()]
    
    a = [int(x) for x in fin.readline().split()]
    
    q = [None] * Q
    for i in range(Q):
        q[i] = tuple([int(x) for x in fin.readline().split()])
    
    fout.write('\n')
    
fin.close()
fout.close()