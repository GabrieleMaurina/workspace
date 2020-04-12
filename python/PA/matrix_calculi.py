identity = lambda n:[[1 if x is y else 0 for x in range(n)]for y in range(n)]
square = lambda n:[[1 + x + y * n for x in range(n)]for y in range(n)]
transpose = lambda m:[[m[x][y] for x in range(len(m))]for y in range(len(m[0]))]
multiply = lambda m0, m1:[[sum([m0[y][i]*m1[i][x] for i in range(len(m1))]) for x in range(len(m1[0]))]for y in range(len(m0))]

m0 = square(2) + [[5, 6]]
m1 = transpose(m0)

print(multiply(m0, m1))