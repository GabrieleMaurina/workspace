#!/usr/bin/env python3

import sys
from heapq import heappop, heappush
from collections import defaultdict

def arg(default):
    arg.next += 1
    if arg.next < len(sys.argv): return sys.argv[arg.next]
    else: return default
arg.next = 0

testNum = arg(4)

sys.stdin = open('input'+str(testNum)+'.txt', 'r')
sys.stdout = open('output'+str(testNum)+'.txt', 'w')

cost = {'#':-1, '~':800, '*':200, '+':150, 'X':120, '_':100, 'H':70, 'T':50}

N, M, C, R = [int(i) for i in input().split()]
X = 0
Y = 1

map = []
customers = []
occupied = []
#  x y reward
for c in range(C):
    (x, y, rew) = [int(i) for i in input().split()]
    customers.append((x,y,rew))
    occupied.append((x,y))
occupied = set(occupied)

# [x][y]
for m in range(M):
    map.append([cost[c] for c in list(input())])
map = [list(x) for x in zip(*map)]


dist = list()

for i in range(C-1):
    (x1, y1, _) = customers[i]
    for j in range(i+1, C):
        (x2, y2, _) = customers[j]
        d = abs(x1-x2) + abs(y1-y2)
        heappush(dist, (d, i, j))


parents = [c for c in range(C)]

def findRoot(i):
    if i == parents[i]: return i
    root = parents[i] = findRoot(parents[i])
    return root

numc = C
while numc > R:
    (_, a, b) = heappop(dist)
    ra = findRoot(a)
    rb = findRoot(b)
    if ra == rb: continue

    parents[rb] = ra
    numc -= 1


for i in range(C):
    findRoot(i)



groups = defaultdict(list)
for i in range(C):
    groups[parents[i]].append(i)
groups = groups.values()


def path(x1, y1, x2, y2):
    def computePath(paths, p):
        p2 = p
        path = []
        while(p in paths):
            path.append(paths[p][0])
            p = paths[p][1]
        return ''.join(reversed(path)), paths[p2][2]
    points = [(0, (x1, y1))]
    visited = set()
    paths = {}
    while(len(points) > 0):
        c, p = heappop(points)
        if p in visited: continue

        visited.add(p)
        if p[X] == x2 and p[Y] == y2:
            return computePath(paths, p)
        else:
            if p[X] > 0 and (p[X]-1, p[Y]) not in visited and map[p[X]-1][p[Y]] != -1:
                heappush(points, (c + map[p[X]-1][p[Y]], (p[X]-1, p[Y])))
                paths[(p[X]-1, p[Y])] = ('L', p, c + map[p[X]-1][p[Y]])
            if p[X] < N-1 and (p[X]+1, p[Y]) not in visited and map[p[X]+1][p[Y]] != -1:
                heappush(points, (c + map[p[X]+1][p[Y]], (p[X]+1, p[Y])))
                paths[(p[X]+1, p[Y])] = ('R', p, c + map[p[X]+1][p[Y]])
            if p[Y] > 0 and (p[X], p[Y]-1) not in visited and map[p[X]][p[Y]-1] != -1:
                heappush(points, (c + map[p[X]][p[Y]-1], (p[X], p[Y]-1)))
                paths[(p[X], p[Y]-1)] = ('U', p, c + map[p[X]][p[Y]-1])
            if p[Y] < M-1 and (p[X], p[Y]+1) not in visited and map[p[X]][p[Y]+1] != -1:
                heappush(points, (c + map[p[X]][p[Y]+1], (p[X], p[Y]+1)))
                paths[(p[X], p[Y]+1)] = ('D', p, c + map[p[X]][p[Y]+1])


offices = []
left = []

for g in groups:
    best = N*M*len(g)
    cbest = 0
    for c1 in g:
        x1, y1, _ = customers[c1]
        tot = 0
        for c2 in g:
            x2, y2, _ = customers[c2]
            dist = abs(x1 - x2) + abs(y1 - y2)
            tot += dist
        if tot < best:
            cbest, best = c1, tot
    (x, y, _) = customers[cbest]

    for (dx, dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
        (xx, yy) = (dx+x, dy+y)
        if xx >= 0 and yy >= 0 and xx < N and yy < M:
            if map[xx][yy] >= 0 and (xx,yy) not in occupied: 
                letter = ''
                if dx == 1: letter = 'L'
                if dx == -1: letter = 'R'
                if dy == 1: letter = 'U'
                if dy == -1: letter = 'D'
                print(xx, yy, letter)
                offices.append((xx, yy))

                for c in g:
                    if c != cbest:
                        x, y, rew = customers[c]
                        res = path(xx, yy, x, y)
                        if res and rew - res[1] > 0 :
                            print(xx, yy, res[0])
                        else:
                            left.append(c)

                break 

for c in left:
    cx, cy, rew = customers[c]
    for u in offices:
        ox, oy = u
        res = path(ox, oy, cx, cy)
        if res and rew - res[1] > 0 :
            print(ox, oy, res[0])
            break



