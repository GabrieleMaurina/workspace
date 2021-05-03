import numpy as np
from numba import njit
from time import time
from sys import argv

N = int(argv[1])
K = int(argv[2])

def rank(a,k):
    return np.sum(a[:k])

def naive_select(a,k):
    tot = 0
    i = -1
    for v in a:
        i+=1
        tot+=v
        if tot>=k: break
    return i

select = njit(naive_select)

def t(f,*args):
    t1 = time()
    v = f(*args)
    t2 = time()
    print(f'{f.__name__} time: {t2-t1}')
    return v

a = np.random.choice(a=(True,False),size=(N,))

print(t(rank,a,K))
print(t(select,a,K))
print(t(naive_select,a,K))
