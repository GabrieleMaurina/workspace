from DNNCTF import DNNCTF
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATASET = 'iris.data'
MODEL = 'model'

df = pd.read_csv(DATASET, header=None)

data = df.iloc[:, :-1]
target = df.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=0)
print('Dataset created.')

classifier = DNNCTF(
    path=MODEL,
    layers =[10, 10, 10],
    learning_rate=0.001,
    steps=1000,
    batch_size=10,
    log=True
    )
print('Classifier instantiated.')

classifier.fit(x_train, y_train)
print('Classifier trained.')

classifier = DNNCTF(path=MODEL, log=False)
print('Classifier restored.')

y_pred = classifier.predict(x_test)
print('Classifier tested')

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
