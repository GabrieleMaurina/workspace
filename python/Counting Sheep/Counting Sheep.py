SMALL = "A-small.in"
LARGE = "A-large.in"

fin = open(SMALL, "r")
fout = open("output.out", "w")

cases = int(fin.readline())

def ok (digits):
    for d in range(10):
        if not digits[d]:
            return False
    return True

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")

    n = int(fin.readline())

    if n == 0:
        fout.write("INSOMNIA")
    else:
        digits = [False] * 10
        k = 1
        number = n
        last = 0
        while(not ok(digits)):
            ds = str(number)
            for d in ds:
                digits[int(d)] = True
            last = number
            k = k + 1
            number = n * k
        fout.write(str(last)) 
    
    fout.write("\n")
    
fin.close()
fout.close()
