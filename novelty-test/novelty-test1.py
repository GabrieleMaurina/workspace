import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.metrics import accuracy_score

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

np.random.seed(1)
np.random.shuffle(points)
np.random.seed(1)
np.random.shuffle(labels)

models, names = [], []

models.append(OneClassSVM(nu=CONTAMINATION))
names.append('svm')

models.append(IsolationForest(contamination=CONTAMINATION))
names.append('isolation_forest')

models.append(EllipticEnvelope(contamination=CONTAMINATION))
names.append('elliptic_envelope')

for model, name in zip(models, names):
	model.fit(points)
	pred = model.predict(points)
	acc = accuracy_score(labels, pred)
	print('%s: accuracy_score %f' % (name, acc))

plt.scatter(regulars.T[0], regulars.T[1], color='green')
plt.scatter(outliers.T[0], outliers.T[1], color='red')

plt.show()