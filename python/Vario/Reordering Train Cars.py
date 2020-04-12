import math

from string import ascii_lowercase
fin = open("input.txt", "r")
fout = open("output.txt", "w")
cases = eval(fin.readline())
for i in range(cases):
    fout.write("Case #" + (str)(i + 1) + ": ")

    fin.readline()

    trains = [car for car in fin.readline().split()]
    toReturn = 1
    for letter in ascii_lowercase:
        start = 0
        end = 0
        full = 0
        for car in trains:
            if car.count(letter) > 0:
                if car.count(letter) == len(car):
                    full = full + 1
                else:
                    if car[0] != letter and car[len(car) - 1] == letter:
                        if not start:
                            start = 1
                            print("start " + letter + " " + car)
                        else:
                            toReturn = 0
                            break

                    if car[0] == letter and car[len(car) - 1] != letter:
                        if not end:
                            end = 1
                            print("end " + letter + " " + car)
                        else:
                            toReturn = 0
                            break
                    
                    if car[0] == letter and car[len(car) - 1] == letter:
                        toReturn = 0
                        break

                    if car[0] != letter and car[len(car) - 1] != letter:
                        if start:
                            toReturn = 0
                            break
                        else:
                            start = 1

                        if end:
                            toReturn = 0
                            break
                        else:
                            end = 1
                            
        toReturn = toReturn * math.factorial(full)
        print(letter + " " + str(toReturn) + " " + str(full))
                
    
    fout.write(str(toReturn) + "\n")
    
fin.close()
fout.close()
