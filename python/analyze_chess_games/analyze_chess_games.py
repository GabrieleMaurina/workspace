import csv
import chess.pgn
import datetime
import os.path


GAMES_PGNS = 'GabrieleMaurina.pgn'
GAMES_PGNS_PATH = os.path.join(os.path.dirname(__file__), GAMES_PGNS)
GAMES_CSV = 'GabrieleMaurina.csv'
GAMES_CSV_PATH = os.path.join(os.path.dirname(__file__), GAMES_CSV)


def load_pgns():
    with open(GAMES_PGNS_PATH) as pgns:
        i = 0
        while game:= chess.pgn.read_game(pgns):
            i += 1
            yield game


def load_games():
    for pgn in load_pgns():
        headers = pgn.headers
        game = {}
        utc_date = headers['UTCDate']
        utc_time = headers['UTCTime']
        game['timestamp'] = datetime.datetime.strptime(utc_date + '-' + utc_time, '%Y.%m.%d-%H:%M:%S').astimezone(datetime.timezone.utc)
        if pgn.headers['White'] == 'gabrielemaurina':
            game['color'] = 'white'
            game['elo'] = int(headers['WhiteElo'])
            game['opponent_elo'] = int(headers['BlackElo'])
            game['score'] = 1 if headers['Result'] == '1-0' else 0 if headers['Result'] == '0-1' else 0.5
        else:
            game['color'] = 'black'
            game['elo'] = int(headers['BlackElo'])
            game['opponent_elo'] = int(headers['WhiteElo'])
            game['score'] = 0 if headers['Result'] == '1-0' else 1 if headers['Result'] == '0-1' else 0.5
        r = headers['Result']
        game['time_control'] = headers['TimeControl']
        yield game


def save_games(games):
    with open(GAMES_CSV_PATH, 'w', newline='') as out:
        csv_writer = csv.DictWriter(out, fieldnames=games[0].keys())
        csv_writer.writeheader()
        for game in games:
            game['timestamp'] = game['timestamp'].isoformat()
            csv_writer.writerow(game)


def main():
    games = tuple(load_games())
    save_games(games)


if __name__ == '__main__':
    main()
