from math import *

fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    N, K = [int(x) for x in fin.readline().split()]
    
    s = {N:1}
    done = 0
    if N == K:
        fout.write("0 0")
    else:
        while s:
            v = max(s)
            vN = s[v]
            del s[v]

            v -= 1
            v /= 2

            right = ceil(v)
            left = floor(v)

            if right > 0:
                s[right] = s.get(right, 0) + vN
            if left > 0:
                s[left] = s.get(left, 0) + vN

            done += vN

            if done >= K:
                fout.write(str(max(right, left)) + " " + str(min(right, left)))
                break
    
    fout.write("\n")
    
fin.close()
fout.close()
