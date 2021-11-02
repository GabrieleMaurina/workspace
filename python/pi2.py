from sys import argv

def pi(v):
    v2 = v**2
    tot = 0
    for x in range(v):
        for z in range(v):
            if x*x+z*z < v2:
                tot += 1
    return tot*4/v2

if __name__=='__main__':
    v = int(argv[1])
    print(pi(v))