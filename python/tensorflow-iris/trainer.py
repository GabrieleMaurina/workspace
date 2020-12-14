from DNNCTF import DNNCTF
import pandas as pd

DATASET = 'iris.data'
MODEL = 'model'

df = pd.read_csv(DATASET, header=None)

data = df.iloc[:, :-1].sample(frac=1, random_state=0)
target = df.iloc[:,-1].sample(frac=1, random_state=0)

print('Dataset created.')

classifier = DNNCTF(
    path=MODEL,
    layers =[10, 10, 10],
    learning_rate=0.001,
    steps=1000,
    batch_size=10,
    del_prev_mod=True,
    log=True
    )
print('Classifier instantiated.')

classifier.fit(data, target)
print('Classifier trained.')