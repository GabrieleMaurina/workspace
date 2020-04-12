fin = open("input.in", "r")
fout = open("output.out", "w")

cases = int(fin.readline())

digits = []

def delete(s, c):
    index = s.find(c)
    s = s[:index] + s[index + 1:]
    return s

def removeNumber(s, k, n, N):
    global digits
    while s.find(k) != -1:
        digits.append(N)
        for c in n:
            s = delete(s, c)
    return s

for i in range(cases):
    fout.write("Case #" + str(i + 1) + ": ")
    digits = []
    s = fin.readline()

    s = removeNumber(s, "Z", "ZERO", 0)
    s = removeNumber(s, "W", "TWO", 2)
    s = removeNumber(s, "X", "SIX", 6)
    s = removeNumber(s, "G", "EIGHT", 8)
    s = removeNumber(s, "U", "FOUR", 4)
    s = removeNumber(s, "F", "FIVE", 5)
    s = removeNumber(s, "T", "THREE", 3)
    s = removeNumber(s, "O", "ONE", 1)
    s = removeNumber(s, "V", "SEVEN", 7)
    s = removeNumber(s, "N", "NINE", 9)

    digits = sorted(digits)

    for d in digits:
        fout.write(str(d))
    
    fout.write("\n")
    
fin.close()
fout.close()
