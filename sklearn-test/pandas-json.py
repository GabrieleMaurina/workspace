import pandas as pd

try:
	df = pd.read_json('{file:"asdf"}', orient='values')
except:
	df = 'asdf'

print(df)