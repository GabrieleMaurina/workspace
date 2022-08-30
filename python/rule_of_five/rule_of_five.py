#!/usr/bin/env python

import numpy as np
from progressbar import progressbar
import matplotlib.pyplot as plt

N = 1000
POPULATION = 100
SAMPLE = tuple(range(2, 8))

DISTRIBUTIONS = (
    ('uniform', np.random.uniform, 'red'),
    ('normal', np.random.normal, 'green'),
    ('poisson', np.random.poisson, 'blue'),
    ('binomial', lambda size: np.random.binomial(10, 0.2, size=size), 'magenta'),
    ('weibull', lambda size: np.random.weibull(10, size=size), 'cyan'))

def compute_probabilities(x, distribution, sample):
    probabilities = []
    for i in x:
        tot = 0
        for j in range(N):
            population = distribution(size=i)
            s = np.random.choice(population, sample)
            mn = min(s)
            mx = max(s)
            median = np.median(population)
            contained = mn <= median <= mx
            if contained:
                tot += 1
        probabilities.append(tot/N)
    return probabilities

def compute_rule(sample, ax):
    x = tuple(range(sample, POPULATION+1))    
    data = [(name, compute_probabilities(x, distribution, sample), color) for name, distribution, color in DISTRIBUTIONS]
    ax.set_title(f'{sample} samples')
    for name, probabilities, color in data:
        ax.plot(x, probabilities, color=color, label=name)
    ax.set(xlabel='population size', ylabel='probability')
    ax.label_outer()
    return ax.get_legend_handles_labels()

def main():
    fig, axs = plt.subplots(len(SAMPLE)//2, 2, sharex=True, sharey=True)
    axs = [col for row in axs for col in row]
    fig.suptitle(f'Rule of Five')
    for sample, ax in progressbar(tuple(zip(SAMPLE, axs))):
        handles, labels = compute_rule(sample, ax)
    fig.legend(handles, labels, loc='upper left')
    fig.tight_layout()
    fig.savefig('rule_of_five.pdf')

if __name__ == '__main__':
    main()
