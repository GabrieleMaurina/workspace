import random as r
import statistics as s

POP_SIZE = 1000000
LAST_NAMES = 1000

class Person:
    def __init__(self, age, sex, lastName):
        self.age = age
        self.sex = sex
        self.lastName = lastName

def init_pop():
    population = set()
    ppln = POP_SIZE // LAST_NAMES
    lastNames = [ppln] * LAST_NAMES
    for lastName in range(LAST_NAMES):
        for i in range(ppln):
            person = Person(r.randrange(70), r.randrange(2), lastName)
            population.add(person)
    return population, lastNames

def death(age):
    return age > r.randint(50, 120) or r.random() < 0.009

def children(age):
    return 15 < age < 50 and r.random() < 0.04

def sim_year(population, lastNames):
    dead = []
    fathers = []
    mothers = []
    births = 0
    
    for person in population:
        person.age += 1
        if death(person.age):
            dead.append(person)
        elif children(person.age):
            if person.sex:
                fathers.append(person)
            else:
                mothers.append(person)
    
    for person in dead:
        population.remove(person)
        lastNames[person.lastName] -= 1
    for father, mother in zip(fathers, mothers):
        for i in range(r.randrange(3) + 1):
            births += 1
            population.add(Person(0, r.randrange(2), father.lastName))
            lastNames[father.lastName] += 1
    
    return births, len(dead)

def main():
    population, lastNames = init_pop()
    year = 0
    while True:
        year += 1
        births, deaths = sim_year(population, lastNames)
        print(f'Year: {year}, Population: {len(population)}, Births: {births}, Deaths: {deaths}, MaxLN: {max(lastNames)}, MinLN: {min(lastNames)}, MeanLN: {int(s.mean(lastNames))}, MedianLN: {int(s.median(lastNames))}')

if __name__ == '__main__':
    main()