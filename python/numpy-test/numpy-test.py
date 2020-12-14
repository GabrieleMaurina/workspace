import numpy as np

CSV = 'numpy.csv'

data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

np.savetxt(CSV, data, delimiter=',')

data = np.loadtxt(CSV, delimiter=',')

print(data)
