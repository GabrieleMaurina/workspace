from graphics import *

X_WIN = 500
Y_WIN = 500
X_MAX = 10
Y_MAX = 10

BACKGROUND = "black"
GREEN = color_rgb(0, 255, 0)
BLUE = color_rgb(0, 0, 255)

def draw(win, color):
    win.setBackground(BACKGROUND)
    r = Rectangle(Point(10, 10), Point(X_WIN - 10, Y_WIN - 10))
    r.setOutline(color)
    r.setWidth(3)
    r.draw(win)
    
    l = Line(Point(10, 10), Point(10, Y_WIN - 10))
    l.setFill(color)
    for i in range(X_MAX):
        l.draw(win)
        l = l.clone()
        l.move((X_WIN - 20) / X_MAX, 0)
        
    l = Line(Point(10, 10), Point(X_WIN - 10, 10))
    l.setFill(color)
    for i in range(Y_MAX):
        l.draw(win)
        l = l.clone()
        l.move(0, (Y_WIN - 20) / Y_MAX)

win = GraphWin('Chain Reaction', X_WIN, Y_WIN)
colors = [GREEN, BLUE]

end = False
turn = 0;
draw(win, colors[turn])
while(not end):
    end = ++end % 2
    draw(win, colors[turn])
