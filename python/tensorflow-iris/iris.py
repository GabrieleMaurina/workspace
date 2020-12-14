import tensorflow as tf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import logging
logging.getLogger().setLevel(logging.INFO)

COLUMNS = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']
CLASSES = ['Iris-virginica','Iris-versicolor', 'Iris-setosa']
COLORS = ['#FF0000', '#00FF00', '#0000FF']
TRAINING = 0.8

df = pd.read_csv('iris.data', header=None).sample(frac=1, random_state=1234)

rows, cols = df.shape

x_train = np.array(df.iloc[:int(rows * TRAINING),:-1]).T
y_train = np.array(df.iloc[:int(rows * TRAINING),-1:]).T[0]

x_test = np.array(df.iloc[int(rows * TRAINING):,:-1]).T
y_test = np.array(df.iloc[int(rows * TRAINING):,-1:]).T[0]

'''colors = [COLORS[CLASSES.index(l)] for l in df[4]]
for i in range(4):
	for j in range(4):
		plt.scatter(df[i], df[j], c=colors)
		plt.show()'''

my_feature_columns = [tf.feature_column.numeric_column(c) for c in COLUMNS]

input_function = tf.estimator.inputs.numpy_input_fn(
		{COLUMNS[i]: c for i, c in enumerate(x_train)},
		np.array([CLASSES.index(l) for l in y_train]),
		shuffle=True, batch_size=10, num_epochs=1000)

eval_input_function = tf.estimator.inputs.numpy_input_fn(
		{COLUMNS[i]: c for i, c in enumerate(x_test)},
		np.array([CLASSES.index(l) for l in y_test]),
		shuffle=False)

classifier = tf.estimator.DNNClassifier(
	feature_columns=my_feature_columns,
	hidden_units=[10, 10, 10],
	n_classes=3,
	optimizer=tf.train.GradientDescentOptimizer(
		learning_rate=0.001
	))
classifier.train(input_fn=input_function, steps=1000)
e = classifier.evaluate(input_fn=eval_input_function)
print(e)

predictions = classifier.predict(input_fn=eval_input_function)

for t, p in zip(y_test, predictions):
	id = p['class_ids'][0]
	predicted = CLASSES[id]
	prob = p['probabilities'][id]
	if(t != predicted):
		print(t + ' ' + predicted + ' ' + str(prob) + '    ERROR!')
