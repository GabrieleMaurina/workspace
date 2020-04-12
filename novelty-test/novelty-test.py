import pandas
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.neighbors import LocalOutlierFactor

regular = pandas.read_csv('iris-novelty.data', header=None)
outliers = pandas.read_csv('iris-novelty-outliers.data', header=None)

svm = OneClassSVM(nu=0.01)
svm.fit(regular)
print(svm.predict(outliers))
print(svm.predict(regular))

isolation_forest = IsolationForest(contamination=0)
isolation_forest.fit(regular)
print(isolation_forest.predict(outliers))
print(isolation_forest.predict(regular))

elliptic_envelope = EllipticEnvelope(contamination=0)
elliptic_envelope.fit(regular)
print(elliptic_envelope.predict(outliers))
print(elliptic_envelope.predict(regular))

local_outlier_factor = LocalOutlierFactor()
local_outlier_factor.fit(regular)
print(local_outlier_factor.predict(outliers))
print(local_outlier_factor.predict(regular))