import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

TRAINING = 0.8

df = pd.read_csv('iris.data', header=None).sample(frac=1, random_state=12345)
rows, cols = df.shape

x_train = df.iloc[:int(rows * TRAINING),:-1]
y_train = df.iloc[:int(rows * TRAINING),-1:]

x_test = df.iloc[int(rows * TRAINING):,:-1]
y_test = df.iloc[int(rows * TRAINING):,-1:]

classifier = MLPClassifier(learning_rate_init=0.01)

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print(accuracy)
