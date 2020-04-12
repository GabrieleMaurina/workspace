#!/usr/bin/env python3

import sys
import heapq
from collections import defaultdict

def arg(default):
    arg.next += 1
    if arg.next < len(sys.argv): return sys.argv[arg.next]
    else: return default
arg.next = 0

testNum = arg(0)

sys.stdin = open('input'+str(testNum)+'.txt', 'r')
sys.stdout = open('output'+str(testNum)+'.txt', 'w')

cost = {'#':-1, '~':800, '*':200, '+':150, 'X':120, '_':100, 'H':70, 'T':50}

N, M, C, R = [int(i) for i in input().split()]

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

offices = []
left = R
for (reward, x, y) in rewards:
    for (dx, dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
        (xx, yy) = (dx+x, dy+y)
        if xx >= 0 or yy >= 0 or xx < N or yy < M:
            if map[xx][yy] >= 0 and (xx,yy) not in occupied: 
                path = ''
                if dx == 1: path = 'L'
                if dx == -1: path = 'R'
                if dy == 1: path = 'D'
                if dy == -1: path = 'U'
                print(xx, yy, path)
                offices.append((xx, yy))
                left -= 1
                break

    if left == 0:
        break




