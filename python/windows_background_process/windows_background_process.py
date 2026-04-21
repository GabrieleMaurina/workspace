import datetime
import os.path
import time


DIR = os.path.normpath(os.path.dirname(__file__))
FILE = os.path.join(DIR, 'background_process.txt')


def main():
    with open(FILE, 'w'):
        pass
    while True:
        time.sleep(3)
        if not os.path.isfile(FILE):
            return
        with open(FILE, 'a') as f:
            f.write(datetime.datetime.now().isoformat() + '\n')


if __name__ == '__main__':
    main()
