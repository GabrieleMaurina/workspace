import string, random
digits = []
digits += string.ascii_lowercase
digits += string.ascii_uppercase
digits += range(10)
for i in range(8):
	print(random.choice(digits), end='')