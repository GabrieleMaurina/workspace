import numpy as np
import numba as nb
from time import time
from sys import argv

N = int(argv[1])
K = int(argv[2])

def rank(a,k):
    return np.sum(a[:k])

@nb.guvectorize([(nb.types.b1[:],nb.types.int64,nb.types.int64[:])],'(n),()->()')
def select(a,k,res):
    tot = 0
    res[0] = -1
    for v in a:
        res[0] += 1
        tot += v
        if tot>=k: break

def t(f,*args):
    t1 = time()
    v = f(*args)
    t2 = time()
    print(f'{f.__name__} time: {t2-t1}')
    return v

#a = np.random.choice(a=(True,False),size=(N,))
a = np.empty(shape=(N,),dtype=np.bool_)

print(t(rank,a,K))
print(t(select,a,K))
