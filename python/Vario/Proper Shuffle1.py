from random import randint

fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())

for i in range(cases):
    fout.write("Case #" + (str)(i + 1)+ " ")
    size = int(fin.readline())
    vet = [int(i) for i in fin.readline().split()]
    prima = 0
    dopo = 0
    p = 0
    d = 0
    for j in range(size):
        if vet[j] < j:
            prima += 1
        elif vet[j] > j:
            dopo += 1
            
    for j in range(size):
        if j <= size // 2:
            p += vet[j]
        else:
            d += vet[j]
    a = 0        
    to_write = ""
    if prima > dopo:
        a -= 1
    elif prima < dopo:
        a += 1
    if p > d:
        a -= 1
    elif p < d:
        a += 1

    if a < 0:
        to_write = "GOOD"
    elif a > 0:
        to_write = "BAD"
    else:
        to_write = "BAD"
    fout.write(to_write + "\n")
    
fin.close()
fout.close()
