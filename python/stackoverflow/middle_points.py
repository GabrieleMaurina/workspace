array = [0,0,0,1,1,1,0,0,1,1,1,1,1,0,0]
array = [0,0,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1]

def middle_points(array):
	indexes = []
	first_one = -1
	for i in range(len(array)):
		if first_one == -1 and array[i] == 1:
			first_one = i
		elif first_one > -1 and array[i] == 0:
			indexes.append((first_one+i-1)//2)
			first_one = -1
	if first_one > -1:
		indexes.append((first_one+len(array)-1)//2)
	return indexes

print(middle_points(array))
