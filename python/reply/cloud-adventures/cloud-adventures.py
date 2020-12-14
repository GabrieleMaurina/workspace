fin = open('adventure.in', 'r')
fout = open('adventure.out', 'w')

V, S, C, P = [int(i) for i in fin.readline().split()]

services = fin.readline().split()
countries = fin.readline().split()
providers = []
projects = []

for v in range(V):
    line = fin.readline().split()
    providers.append((line[0], int(line[1]), []))
    for rv in range(providers[-1][1]):
        region = fin.readline()[:-1]
        line = fin.readline().split()
        providers[-1][2].append((region, int(line[0]), float(line[1]), [int(i) for i in line[2:]], [int(i) for i in fin.readline().split()]))

print(providers)

for p in range(P):
    line = fin.readline().split()
    projects.append((int(line[0]), line[1], [int(i) for i in line[2:]]))
print(projects)

fout.close()
fin.close()
