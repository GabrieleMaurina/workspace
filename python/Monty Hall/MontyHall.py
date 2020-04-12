import random

TOT = 100
w1 = 0
w1 = 0

for i in range(TOT):
    d = random.randint(0, 2)
    p = random.randint(0, 2)
    if p == d:
        w1 += 1
    doors = [True, True, True]
    doors[d] = False
    doors[p] = False
    s = 0
    for e in range(3):
        if doors[e]:
            s = e
    if

print(str(int(w1 / TOT * 100)) + "%")
print(str(int(w2 / TOT * 100)) + "%")
    
