import math

def fi(maxD):
    if maxD < 0:
        return 0
    return math.sqrt(1 + fi(maxD - 1))

print("Fi vale: " + str(fi(50)))
