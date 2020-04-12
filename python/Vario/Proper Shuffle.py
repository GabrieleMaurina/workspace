from random import randint

fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
casi = 100
lunghezza = 10
tot = 0
for i in range(casi):
    #line = fin.readline()
    #fout.write("Case #" + (str)(i + 1))
    vet = [x for x in range(lunghezza)]
    prima = 0
    dopo = 0
    p = 0
    d = 0
    punteggio = 0
    for j in range(lunghezza):
        k = randint(j, lunghezza - 1)
        a = vet[k]
        vet[k] = vet[j]
        vet[j] = a
    for j in range(lunghezza):
        fout.write(str(vet[j]) + " ")
        if vet[j] < j:
            prima += 1
        elif vet[j] > j:
            dopo += 1
            
    #for j in range(lunghezza):
    #    if j <= lunghezza // 2:
     #       p += vet[j]
     #   else:
     #       d += vet[j]

    fout.write("prima: " + str(prima) + " dopo: " + str(dopo) + "\n")
    if prima > dopo:
        tot -= 1
    elif prima < dopo:
        tot += 1
    if p > d:
        tot -= 1
    elif p < d:
        tot += 1

fout.write("tot = " + str(tot) + "\n\n")

tot = 0
for i in range(casi):
    
    vet = [x for x in range(lunghezza)]
    prima = 0
    dopo = 0
    p = 0
    d = 0
    for j in range(lunghezza):
        k = randint(0, lunghezza - 1)
        a = vet[k]
        vet[k] = vet[j]
        vet[j] = a
        
    for j in range(lunghezza):
        fout.write(str(vet[j]) + " ")
        if vet[j] < j:
            prima += 1
        elif vet[j] > j:
            dopo += 1
            
    #for j in range(lunghezza):
    #    if j <= lunghezza // 2:
     #       p += vet[j]
     #   else:
      #      d += vet[j]
    
    fout.write("prima: " + str(prima) + " dopo: " + str(dopo) + "\n")
    if prima > dopo:
        tot -= 1
    elif prima < dopo:
        tot += 1

    if p > d:
        tot -= 1
    elif p < d:
        tot += 1

fout.write("tot = " + str(tot) + "\n\n")
    
fin.close()
fout.close()
