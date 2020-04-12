fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    N = int(fin.readline())
    numbers = {}
    res = []
    for e in range(2 * N - 1):
        for n in fin.readline().split():
            n = int(n)
            numbers[n] = numbers.get(n, 0) + 1
  
    for n in numbers:
        if n % 2 == 1:
            res.append(n)

    res = sorted(res)

    for n in res:
        fout.write(str(n) + " ")
    
    fout.write("\n")
    
fin.close()
fout.close()
