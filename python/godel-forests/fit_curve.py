#!/usr/bin/env python

# Copyright 2020 by Gabriele Maurina, Università degli Studi di Milano.
# All rights reserved.
# This file is released under the "MIT License Agreement".

import numpy as np
from scipy.optimize import curve_fit as fit
import matplotlib.pyplot as plt

def f(x, a):
	return np.power(a, x)

x, y = (np.delete(v, 0) for v in np.genfromtxt('./count.txt', delimiter=',').transpose())

p = fit(f, x, y, p0=[1.048], bounds=([1], [1.2]))[1]

print(p)

plt.plot(x, y, 'b-', label='original')
plt.plot(x, f(x, *p), 'r-', label='function')

plt.xlabel('K')
plt.ylabel('Fine(K)')
plt.legend()
plt.show()
