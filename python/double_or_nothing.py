from random import random as rand
from sys import argv

def main():
	probabilty = float(argv[1])
	capital = int(argv[2])
	bet = int(argv[3])

	while capital > 0:
		print(f'Capital = {capital}, Bet = {bet}')
		win = probabilty > rand()
		if win:
			capital += bet
			break
		else:
			capital -= bet
			bet *= 2

	print(f'Capital = {capital}, Bet = {bet}')

if __name__ == '__main__':
	main()
