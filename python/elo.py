from numpy import full
from numpy.random import normal as normal, randint as randint

N_PLAYERS = 1000
N_GAMES = 10000000
STARTING_ELO = 1500.0
MAX_ELO_DIFF = 100.0
DRAW_DIFF = 0.01
PERFORMANCE_SD = 0.1
K = 16

def main():
    strength = normal(size=N_PLAYERS)
    elo = full(N_PLAYERS, STARTING_ELO)
    for game in range(N_GAMES):
        while True:
            p1 = randint(N_PLAYERS)
            p2 = randint(N_PLAYERS)
            if p1 != p2 and abs(elo[p1]-elo[p2]) < MAX_ELO_DIFF: break
        strength1 = strength[p1]
        strength2 = strength[p2]
        performance1 = normal()*PERFORMANCE_SD + strength1
        performance2 = normal()*PERFORMANCE_SD + strength2
        score1 = 1.0 if performance1 > performance2 + DRAW_DIFF else 0.0 if performance2 > performance1 + DRAW_DIFF else 0.5
        score2 = 1.0 - score1
        elo1 = elo[p1]
        elo2 = elo[p2]
        q1 = pow(10.0, elo1/400.0)
        q2 = pow(10.0, elo2/400.0)
        expected1 = q1 / (q1 + q2)
        expected2 = q2 / (q1 + q2)
        update1 = K * (score1 - expected1)
        update2 = K * (score2 - expected2)
        newelo1 = elo1 + update1
        newelo2 = elo2 + update2
        elo[p1] = newelo1
        elo[p2] = newelo2
        
        res = (game, elo.min(), elo.max(), elo1, elo2, score1, score2, update1, update2)
        print(' '.join(str(int(v)) for v in res))

if __name__ == '__main__':
    main()