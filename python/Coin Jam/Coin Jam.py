import math

N = 32
J = 500

def inc(c):
    index = 1
    while c[index] == 1:
        c[index] = 0
        index += 1
        if index >= len(c):
            return
    c[index] = 1

def prime(n):

    if n % 2 == 0:
            return 2
    for d in range(3, 100, 2):
        if n % d == 0:
            return d
    return 0

def toStr(c):
    number = ""
    for d in reversed(coin):
        number += str(d)
    return number

fout = open("output.out", "w")

fout.write("Case #1:\n")

coin = [0] * N
coin[0] = 1
coin[N - 1] = 1

for i in range(J):
    ds = []
    number = 0
    while True:
        inc(coin)
        number = toStr(coin)
        ok = True
        ds = []
        for base in range(2, 11):
            n = int(number, base)
            d = prime(n)
            if d == 0:
                ok = False
                break
            else:
                ds.append(d)
        if ok:
            break

    fout.write(toStr(coin) + " ")
    for d in ds:
       fout.write(str(d) + " ")
    fout.write("\n")
    
fout.close()
