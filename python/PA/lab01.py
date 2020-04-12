'''from calendar import *

def next_leap(year):
	while not isleap(year):
		year += 1
	return year
print(next_leap(2018))

def next_leap1(year):
	return year if isleap(year) else next_leap1(year + 1)
print(next_leap1(2018))

print(leapdays(2000, 2051))

print(day_name[weekday(2016, 7, 29)])'''

from functools import *

alkaline_earth_metals = [(56, 'barium'), (4, 'beryllium'), (20, 'calcium'), (12, 'magnesium'), (88, 'radium'), (38, 'strontium')]

print(reduce(lambda e0,e1: e0 if e0[0]>e1[0] else e1, alkaline_earth_metals)[0])
print(sorted(alkaline_earth_metals))

alkaline_earth_metals = {m[1]:m[0] for m in alkaline_earth_metals}
print(alkaline_earth_metals)

noble_gases = {'helium': 2, 'neon': 10, 'argon': 18, 'krypton': 36, 'xenon' : 54, 'radon' : 86}
print(noble_gases)

print(sorted([(e[0], e[1]) for e in {**alkaline_earth_metals, **noble_gases}.items()]))