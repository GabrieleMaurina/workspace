import numpy as np
import matplotlib.pyplot as plt

GROUP = 200
OUT = 50
TOT = GROUP * 2 + OUT
CONTAMINATION = OUT / TOT

np.random.seed(1)

g0 = np.random.randn(GROUP, 2) + 4
g1 = np.random.randn(GROUP, 2) - 4
regulars = np.vstack([g0, g1])
outliers = np.random.rand(OUT, 2) * 30 - 15

points = np.vstack([regulars, outliers])
labels = np.hstack([np.ones(GROUP * 2), np.ones(OUT) * -1])

ds = np.hstack([points, np.array([labels]).T])

np.savetxt('points.data', ds, fmt='%.3f', delimiter=',')

plt.scatter(regulars.T[0], regulars.T[1], color='green')
plt.scatter(outliers.T[0], outliers.T[1], color='red')

plt.show()