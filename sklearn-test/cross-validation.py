import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

TRAINING = 0.8

df = pd.read_csv('iris.data', header=None).sample(frac=1, random_state=12345)

data = df.iloc[:, :-1]
target = df.iloc[:,-1]

clf = SVC()

clf.fit(data, target)
clf.fit(data, target)
scores = cross_val_score(clf, data, target, cv=5)
y_pred = clf.predict(data)

accuracy = accuracy_score(target, y_pred)

print(scores.mean())
print(accuracy)
