from random import randint

def printField(field):
    for y in range(len(field[0])):
        for x in range(len(field)):
            print(" " + field[x][y], end = "")
            if x < len(field) - 1:
                print(" |", end = "")
        print()
        if y < len(field[0]) - 1:
            for x in range(len(field) * 4 - 1):
                print("-", end = "")
            print()
    print()
    print()

def end(field, length):
    full = True
    X_SIZE = len(field)
    Y_SIZE = len(field[0])
    for y in range(len(field[0])):
        for x in range(len(field)):
            p = field[x][y]
            if p == " ":
                full = False
            hor, ver, dd, du = [True for i in range(4)]
            for i in range(1, length):
                if x + i >= X_SIZE or field[x + i][y] != p:
                    hor = False
                if y + i >= X_SIZE or field[x][y + i] != p:
                    ver = False
                if x + i >= X_SIZE or y + i >= X_SIZE or field[x + i][y + 1] != p:
                    dd = False
                if x + i >= X_SIZE or y - i < 0 or field[x + i][y - i] != p:
                    du = False
            if hor or ver or dd or du:
                return p
    return "#" if full else " "

def player(field):
    ok = False
    while not ok:
        print("POS: ", end = "")
        try:
            x, y  = [int(n) for n in input().split()]
            if x >= 0 and y >= 0 and x < len(field) and y < len(field[0]) and field[x][y] == " ":
                ok = True
                field[x][y] = "X"
            else:
                print("Select an empty spot")
        except:
            print("Write: X Y")
    print("PLAYER")

def otherString(string):
    if string == "X":
        return "O"
    elif string == "O":
        return "X"

def bestMove(field, string, length, index):
    #print(index)
    winner = end(field, length)
    if winner == "#":
        return 0
    elif winner == otherString(string):
        return -1
    else:
        best = -1
        for y in range(len(field[0])):
            for x in range(len(field)):
                if field[x][y] == " ":
                    field[x][y] = string
                    res = bestMove(field, otherString(string), length, index + 1)
                    if res == -1:
                        field[x][y] = " "
                        return 1
                    elif res == 1:
                        res = 1

                    if res > best:
                        best = res
                    field[x][y] = " "
                        
        return best

def bot(field, length):
    print("BOT")
    best = -1
    moves = []
    for y in range(len(field[0])):
        for x in range(len(field)):
            print(str(x) + " " + str(y))
            res = bestMove(field, "O", length, 0)
            if res == best:
                moves.append([x, y])
            elif res > best:
                best = res
                moves = []
                moves.append([x, y])
    move = moves[randint(0, len(moves) - 1)]
    field[move[0]][move[1]] = "O"

play = True
while(play):
    print("X size: ", end = "")
    X_SIZE = int(input())
    print("Y size: ", end = "")
    Y_SIZE = int(input())
    print("Length: ", end = "")
    LENGTH = int(input())
    
    field = [[' '  for i in range(Y_SIZE)] for e in range(X_SIZE)]
    print()
    printField(field)

    turn = randint(0, 1)
    while end(field, LENGTH) == " ":
        if turn == 0:
            player(field)
        else:
            bot(field, LENGTH)
        turn += 1
        turn %= 2
        printField(field)

    res = end(field, LENGTH)
    if res == "#":
        print("***TIE!!!***")
    else:
        print("***" + res + " WINS!!!***");
    
    print("Play again?")
    if input().lower() != "yes":
        play = False
