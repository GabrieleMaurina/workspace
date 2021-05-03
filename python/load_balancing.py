from sys import argv
from random import randrange
from operator import itemgetter

N = int(argv[1])
K = int(argv[2])

jobs = sorted(tuple(randrange(1,1000)for i in range(N)),reverse=True)
loads = [0]*K

for j in jobs:
	loads[min(enumerate(loads),key=itemgetter(1))[0]] += j

print(max(loads))
