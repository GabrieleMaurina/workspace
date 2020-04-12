fin = open('input.in', 'r')
fout = open('output.out', 'w')

cases = int(fin.readline())

for i in range(cases):
    fout.write('Case #' + str(i + 1) + ":")
    
    N = int(fin.readline())
    ts = [(None, None)] * N
    for i in range(N):
        s = fin.readline().replace('\n','')  
        d = fin.readline().replace('\n','')  
        ts[i] = (s, d)
    
    i = [ts[0]]
    del ts[0]
    while len(ts) > 0:
        for t in ts:
            if i[0][0] == t[1]:
                i.insert(0, t)
                ts.remove(t)
                break
            elif i[len(i) - 1][1] == t[0]:
                i.append(t)
                ts.remove(t)
                break
    
    for t in i:
        fout.write(' ' + str(t[0]) + '-' + str(t[1]))
    
    fout.write('\n')
    
fin.close()
fout.close()