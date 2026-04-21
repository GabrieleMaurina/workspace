import random

MONEY = 10000
BET = 25
SESSION_GAIN = 1000

def play_round():
    return random.choice((True, False))

def play_session(start_money):
    money = start_money
    rounds = 0
    while money - start_money < SESSION_GAIN:
        if money < BET:
            print('Bankrupt.')
            exit()
        rounds += 1
        print(f'Playing round {rounds}...')
        if play_round():
            money += BET
            print(f'WIN, current balance: {money}')
        else:
            money -= BET
            print(f'LOSS, current balance: {money}')
    print(f'Session ended in {rounds} rounds with final score {money}.')
    return money, rounds


def sim():
    sessions = 0
    rounds = 0
    money = MONEY
    while True:
        sessions += 1
        print(f'Starting session {sessions}...')
        money, session_rounds = play_session(money)
        rounds += session_rounds
        print(f'Completed {sessions} sessions and {rounds} rounds so far.\nCurrent balance: ${money}')
        input()


def main():
    sim()


if __name__ == '__main__':
    main()
