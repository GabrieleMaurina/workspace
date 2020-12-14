import sys
from heapq import heappush, heappop

fin = open('1_victoria_lake.txt', 'r')

COST = {'#':-1, '~':800, '*':200, '+':150, 'X':120, '_':100, 'H':70, 'T':50}

X, Y = 0, 1

N, M, C, R = [int(i) for i in fin.readline().split()]

customers = []
map = []

for c in range(C):
    customers.append(tuple([int(i) for i in fin.readline().split()]))

for m in range(M):
    map.append([COST[c] for c in list(fin.readline().split()[0])])
map = [list(x) for x in zip(*map)]

def path(x1, y1, x2, y2):
    def computePath(paths, p):
        path = []
        while(p in paths):
            path.append(paths[p][0])
            p = paths[p][1]
        return ''.join(reversed(path))
    points = [(0, (x1, y1))]
    visited = set()
    paths = {}
    while(len(points) > 0):
        c, p = heappop(points)
        visited.add(p)
        if p[X] == x2 and p[Y] == y2:
            return computePath(paths, p)
        else:
            if p[X] > 0 and (p[X]-1, p[Y]) not in visited and map[p[X]-1][p[Y]] != -1:
                heappush(points, (c + map[p[X]-1][p[Y]], (p[X]-1, p[Y])))
                paths[(p[X]-1, p[Y])] = ('L', p)
            if p[X] < N-1 and (p[X]+1, p[Y]) not in visited and map[p[X]+1][p[Y]] != -1:
                heappush(points, (c + map[p[X]+1][p[Y]], (p[X]+1, p[Y])))
                paths[(p[X]+1, p[Y])] = ('R', p)
            if p[Y] > 0 and (p[X], p[Y]-1) not in visited and map[p[X]][p[Y]-1] != -1:
                heappush(points, (c + map[p[X]][p[Y]-1], (p[X], p[Y]-1)))
                paths[(p[X], p[Y]-1)] = ('U', p)
            if p[Y] < M-1 and (p[X], p[Y]+1) not in visited and map[p[X]][p[Y]+1] != -1:
                heappush(points, (c + map[p[X]][p[Y]+1], (p[X], p[Y]+1)))
                paths[(p[X], p[Y]+1)] = ('D', p)

for c1 in reversed(customers):
    for c2 in customers:
        print(path(c1[0], c1[1], c2[0], c2[1]))

fin.close()
