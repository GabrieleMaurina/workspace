from graphics import *
import time
#import pymouse

X_SIZE = 200
Y_SIZE = 150
X_RATIO = 5
Y_RATIO = 5

win = GraphWin('Game Of Py', X_SIZE * X_RATIO, Y_SIZE * Y_RATIO)
win.setBackground('black')

'''mouse = pymouse.PyMouse()
print(win.getMouse())
print(mouse.position())'''

m1 = [[False for y in range(Y_SIZE)] for x in range(X_SIZE)]

def getCell(x, y):
    p1 = Point(x * X_RATIO, y * Y_RATIO)
    p2 = Point((x + 1) * X_RATIO, (y + 1) * Y_RATIO)
    return Rectangle(p1, p2)

def on(x, y):
    rect = getCell(x, y)
    rect.setFill('white')
    rect.draw(win)
    m1[x][y] = True

def off(x, y):
    rect = getCell(x, y)
    rect.setFill('black')
    rect.draw(win)
    m1[x][y] = False

def flip(x, y):
    if m1[x][y]:
        off(x, y)
    else:
        on(x, y)

def refresh():
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if m1[x][y] != m2[x][y]:
                flip(x, y)

def neighbors(x, y):
    tot = 0
    i = 0
    for dx in range(3):
        for dy in range(3):
            i += 1
            nx = x + dx - 1
            ny = y + dy - 1
            if (nx != x or ny != y) and nx > -1 and ny > -1 and nx < X_SIZE and ny < Y_SIZE and m1[nx][ny]:
                tot += 1
    return tot

while True:
    p = win.getMouse()
    p.x = p.x // X_RATIO
    p.y = p.y // Y_RATIO
    if m1[p.x][p.y]:
        break
    else:
        flip(p.x, p.y)


while True:
    m2 = [[False for y in range(Y_SIZE)] for x in range(X_SIZE)]
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            n = neighbors(x, y)
            if m1[x][y]:
                if n == 2 or n == 3:
                    m2[x][y] = True
            elif n == 3:
                m2[x][y] = True
    refresh()
    time.sleep(0.01)

win.close() 
