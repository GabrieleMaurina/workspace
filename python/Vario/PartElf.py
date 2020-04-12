from fractions import Fraction

fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())

for i in range(cases):
    fout.write("Case #" + (str)(i + 1) + ": ")
    times = 1
    a = Fraction(fin.readline())

    while a.denominator % 2 == 0:
        a = a * 2
        if a < 1:
            times += 1

    if a >= 1 and times < 41 and a.denominator == 1:
        fout.write(str(times) + "\n")
    else:
        fout.write("impossible\n")
    
fin.close()
fout.close()
