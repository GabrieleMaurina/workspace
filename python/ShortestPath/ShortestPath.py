import copy

migliore = 10000
perc = []

def Percorso(campo, x0, y0, x1, y1, lun):
    global migliore
    global perc
    campo[x0][y0] = 2
    
    if x0 == x1 and y0 == y1:
        if migliore > lun:
            migliore = lun
            perc = []
        if lun == migliore:
            perc.append(copy.deepcopy(campo))
        campo[x0][y0] = 0
        return
    
    lun += 1
    
    if y0 > 0 and campo[x0][y0 - 1] == 0:
        Percorso(campo, x0, y0 - 1, x1, y1, lun)
    
    if y0 + 1 < len(campo[x0]) and campo[x0][y0 + 1] == 0:
        Percorso(campo, x0, y0 + 1, x1, y1, lun)
        
    if x0 > 0 and campo[x0 - 1][y0] == 0:
        Percorso(campo, x0 - 1, y0, x1, y1, lun)
        
    if x0 + 1 < len(campo) and campo[x0 + 1][y0] == 0:
        Percorso(campo, x0 + 1, y0, x1, y1, lun)
        
    campo[x0][y0] = 0
        

fin = open("input.in", "r")
fout = open("output.out", "w")

x0, y0 = [int(n) for n in fin.readline().split()]
x1, y1 = [int(n) for n in fin.readline().split()]

lines = []
while(True):
    line = fin.readline()
    if line == "":
        break
    lines.append(line.split()[0])

field = [[0 for y in range(len(lines))] for x in range(len(lines[0]))]

for y in range(len(lines)):
    for x in range(len(lines[y])):
        field[x][y] = int(lines[y][x])

print(x0)
print(y0)
print(x1)
print(y1)
print(field)

Percorso(field, x0, y0, x1, y1, 0)

fout.write(str(migliore) + "\n\n")

for p in perc:
    for y in range(len(p[0])):
        for x in range(len(p)):
            fout.write(str(p[x][y]))
        fout.write("\n")
    fout.write("\n")
    
fin.close()
fout.close()
