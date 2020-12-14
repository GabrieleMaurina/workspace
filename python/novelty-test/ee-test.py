from pandas import DataFrame
from sklearn.covariance import EllipticEnvelope

ee = EllipticEnvelope()

m = DataFrame([[1, 0], [0, 1]])
print(m)

ee.fit(m)