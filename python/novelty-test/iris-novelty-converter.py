import sys
import pandas

if len(sys.argv) > 1:
	ds = sys.argv[1]
else:
	ds = 'iris.data'

if len(sys.argv) > 2:
	reg = sys.argv[2]
else:
	reg = 'iris-novelty.data'

if len(sys.argv) > 3:
	out = sys.argv[3]
else:
	out = 'iris-novelty-outliers.data'

if len(sys.argv) > 4:
	outlier = sys.argv[4]
else:
	outlier = 'Iris-virginica'

df = pandas.read_csv(ds, header=None)

regular = df.loc[df[4] != outlier].drop(4, axis=1)
outliers = df.loc[df[4] == outlier].drop(4, axis=1)

regular.to_csv(reg, header=None, index=False)
outliers.to_csv(out, header=None, index=False)