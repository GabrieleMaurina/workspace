from random import randrange as rr
N = 5
I = 1000000

t = [0 for i in range(N)]

for p in range(N):
    for i in range(I):
        if p == 0: p+=1
        elif p == N-1: p-=1
        else: p += 1 if rr(2) else -1
        t[p] += 1

print(t)