from numpy.random import rand
from matplotlib import pyplot as plt

N = 1000

plt.scatter(rand(N) * N, rand(N) * N)
plt.show()