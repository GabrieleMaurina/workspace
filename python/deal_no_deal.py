import random
import sys


def main():
    n_players = int(sys.argv[1])
    if n_players < 2:
        print('Number of players must be at least 2')
        return
    n_passes = int(sys.argv[2])
    if n_passes < 1:
        print('Number of passes must be at least 1')
        return
    n_rounds = int(sys.argv[3])
    if n_rounds < 1:
        print('Number of rounds must be at least 1')
        return
    suvive_count = [0 for _ in range(n_players)]
    for _ in range(n_rounds):
        first = 0
        second = 1
        passes = [True if i < n_passes else False for i in range(n_players)]
        random.shuffle(passes)
        while second < n_players:
            safe = passes.pop(0)
            steal = bool(random.getrandbits(1))
            if safe:
                if steal:
                    suvive_count[second] += 1
                else:
                    suvive_count[first] += 1
            if steal:
                second += 1
            else:
                first = second
                second += 1
        if passes[0]:
            suvive_count[first] += 1
    survive_rate = [int(round(count / n_rounds * 100))
                    for count in suvive_count]
    print('Number of players:', n_players)
    print('Number of passes:', n_passes)
    print('Survival rate:')
    for i, rate in enumerate(survive_rate, 1):
        print(f'Player {i}: {rate}%')


if __name__ == '__main__':
    main()
