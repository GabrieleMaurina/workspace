import random as r
import matplotlib.pyplot as plt

POP_SIZE = 1000000
LAST_NAMES = 1000
MAX_YEAR = 10000
PLOT = 'last_names.pdf'

class Person:
    def __init__(self, age, lastName):
        self.age = age
        self.lastName = lastName

def init_pop():
    population = set()
    ppln = POP_SIZE // LAST_NAMES
    lastNames = [[ppln] for i in range(LAST_NAMES)]
    for lastName in range(LAST_NAMES):
        for i in range(ppln):
            person = Person(r.randrange(70), lastName)
            population.add(person)
    return population, lastNames

def death(age):
    return age > r.randint(50, 120) or r.random() < 0.009

def children(age):
    return 15 < age < 50 and r.random() < 0.02

def sim_year(population, lastNames):
    dead = []
    babies = []
    
    for lastName in lastNames:
        lastName.append(lastName[-1])
    
    for person in population:
        person.age += 1
        if death(person.age):
            dead.append(person)
        elif children(person.age):
            for i in range(r.randrange(3) + 1):
                babies.append(Person(0, person.lastName))
                lastNames[person.lastName][-1] += 1
    
    for person in dead:
        population.remove(person)
        lastNames[person.lastName][-1] -= 1
    for baby in babies:
        population.add(baby)
    
    diff = len(population) - POP_SIZE
    if diff > 0:
        for person in r.sample(population, diff):
            population.remove(person)
            dead.append(person)
    
    return len(babies), len(dead)

def plot(lastNames):
    plt.title('Last Names')
    for lastName in lastNames:
        plt.plot(lastName, color='blue', linewidth=.5)
    plt.savefig(PLOT)
    plt.close()

def main():
    population, lastNames = init_pop()
    try:
        for year in range(MAX_YEAR):
            births, deaths = sim_year(population, lastNames)
            print(f'Year: {year}, Population: {len(population)}, Births: {births}, Deaths: {deaths}')
    finally:
        plot(lastNames)

if __name__ == '__main__':
    main()