Celsius, CelsiusUnit = 'Celsius', 'C'
Fahrenheit, FahrenheitUnit = 'Fahrenheit', 'F'
Kelvin, KelvinUnit = 'Kelvin', 'K'
Rankine, RankineUnit = 'Rankine', 'R'
Delisle, DelisleUnit = 'Delisle', 'De'
Newton, NewtonUnit = 'Newton', 'N'
Réaumur, RéaumurUnit = 'Réaumur', 'Ré'
Rømer, RømerUnit = 'Rømer', 'Rø'

scales = {Celsius:CelsiusUnit, Fahrenheit:FahrenheitUnit, Kelvin:KelvinUnit, Rankine:RankineUnit, Delisle:DelisleUnit, Newton:NewtonUnit, Réaumur:RéaumurUnit, Réaumur:RéaumurUnit, Rømer:RømerUnit}

CToC = lambda v : v

CToF = lambda v : v * (9/5) + 32
CToK = lambda v : v + 273.15
CToR = lambda v : (v + 273.15) * (9/5)
CToDe = lambda v : (100 - v) * (3/2)
CToN = lambda v : v * (33/100)
CToRé = lambda v : v * (4/5)
CToRø = lambda v : v * (21/40) +7.5

FToC = lambda v : (v - 32) * (5/9)
KToC = lambda v : v - 273.15
RToC = lambda v : (v - 491.67) * (5/9)
DeToC = lambda v : 100 - v  * (2/3)
NToC = lambda v : v * (100/300)
RéToC = lambda v : v * (5/4)
RøToC = lambda v : (v - 7.5) * (40/21)

fromC = {CelsiusUnit:CToC, FahrenheitUnit:CToF, KelvinUnit:CToK, RankineUnit:CToR, DelisleUnit:CToDe, NewtonUnit:CToN, RéaumurUnit:CToRé, RømerUnit:CToRø}
toC = {CelsiusUnit:CToC, FahrenheitUnit:FToC, KelvinUnit:KToC, RankineUnit:RToC, DelisleUnit:DeToC, NewtonUnit:NToC, RéaumurUnit:RéToC, RømerUnit:RøToC}

def table(v):
	t = [[fromC[scales[u1]](toC[scales[u0]](v)) for u1 in scales] for u0 in scales]
	res = '   '+(8*'{: ^6} ')+'\n'+(8*('{:<3}'+(8*'{: 6.1f} ')+'\n'))
	tmp = vres = list(scales.values())
	for i in range(8): vres += [tmp[i]] + t[i]
	return res.format(*vres)

def toAll(v, u):
	res=(7*'{{{}[0]:.1f}}°{{{}[1]}} ').format(*[i for s in zip(range(7), range(7)) for i in s])
	return res.format(*sorted([(fromC[scales[unit]](toC[u](v)), scales[unit]) for unit in scales if scales[unit] != u], key=lambda x:x[0]))

if __name__ == '__main__':
	print(table(25))
	print('25°F corresponds to {}'.format(toAll(25, FahrenheitUnit)))