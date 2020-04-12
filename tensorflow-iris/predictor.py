from DNNCTF import DNNCTF
import pandas as pd
from sklearn.metrics import accuracy_score

DATASET = 'iris.data'
MODEL = 'model'

df = pd.read_csv(DATASET, header=None)

data = df.iloc[:, :-1]
target = df.iloc[:,-1]

classifier = DNNCTF(path=MODEL)
print('Classifier restored.')

y_pred = classifier.predict(data)
print('Classifier tested')

accuracy = accuracy_score(target, y_pred)
print(accuracy)