def row_index(array,m,n):
	for index, row in enumerate(array):
		if m in row and n in row:
			yield index
