from random import randrange as rand
from random import choice as rand_choice

TOT = 1000000

switch_wins = 0
no_switch_wins = 0

for i in range(TOT):
	car = rand(3)
	choice = rand(3)
	opened = rand_choice([n for n in range(3) if n != car and n != choice])
	if car == choice:
		no_switch_wins += 1
	else:
		switch_wins += 1

switch_win_rate = switch_wins / TOT * 100
no_switch_win_rate = no_switch_wins / TOT * 100

print(switch_win_rate, no_switch_win_rate)
