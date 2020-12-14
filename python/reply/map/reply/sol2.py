#!/usr/bin/env python3

import sys
from heapq import heappop, heappush
from collections import defaultdict

def arg(default):
    arg.next += 1
    if arg.next < len(sys.argv): return sys.argv[arg.next]
    else: return default
arg.next = 0

testNum = arg(2)

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

rewards = []
for c in range(C):
	(x, y, rew) = customers[c]
	rewards.append((rew - map[x][y], x, y))

rewards.sort(reverse=True)

def allpaths(x1, y1):
    


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
        if p in visited: continue

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

offices = []
left = R
for reward, x, y in rewards:
    if left == 0:
        cx, cy = offices[0]
        mindist = abs(cx - x) + abs(cy - y)
        for ox, oy in offices:
            dist = abs(ox - x) + abs(oy - y)
            if dist < mindist:
                cx, cy, mindist = ox, oy, dist

        pp = path(cx, cy, x, y)

        if pp:
            print(cx, cy, pp)


    else :
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
                    left -= 1
                    break






