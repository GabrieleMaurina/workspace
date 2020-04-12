from math import log2, pow
fin = open('input.in', 'r')
fout = open('output.out', 'w')

cases = int(fin.readline())

for i in range(cases):
    fout.write('Case #' + str(i + 1) + ": ")
    
    K = int(fin.readline())
    
    res = 0
    
    while K > 0:
        e = int(log2(K))
        p2 = pow(2, e)
        r = K - p2
        
        if r == 0:
            res = 0
            break
        elif r == p2 / 2:
            res = 1
            break
        else:
            K = r
    
    fout.write(str(res) + '\n')
    
fin.close()
fout.close()
