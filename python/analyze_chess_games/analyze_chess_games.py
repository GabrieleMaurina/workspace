import chess.pgn
import datetime
import os.path


FILE = 'GabrieleMaurina.pgn'
FILE_PATH = os.path.join(os.path.dirname(__file__), FILE)


def load_pgns():
    with open(FILE_PATH) as pgn:
        i = 0
        while game:= chess.pgn.read_game(pgn):
            i += 1
            yield game
            if i > 10:
                break


def load_games():
    for pgn in load_pgns():
        game = {}
        utc_date = pgn.headers['UTCDate']
        utc_time = pgn.headers['UTCTime']
        game['timestamp'] = datetime.datetime.strptime(utc_date + '-' + utc_time, '%Y.%m.%d-%H:%M:%S')
        if pgn.headers['White'] == 'gabrielemaurina':
            game['elo'] = int(pgn.headers['WhiteElo'])
            game['opponent_elo'] = int(pgn.headers['BlackElo'])
        else:
            game['elo'] = int(pgn.headers['BlackElo'])
            game['opponent_elo'] = int(pgn.headers['WhiteElo'])
        yield game


def main():
    games = tuple(load_games())
    print(games)


if __name__ == '__main__':
    main()
