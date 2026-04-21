import os.path
import subprocess
import time


DIR = os.path.normpath(os.path.dirname(__file__))
FILE = os.path.join(DIR, 'windows_background_process.py')
CMD = 'powershell -Command start -FilePath python -ArgumentList "{}" -WindowStyle Hidden'


def main():
    print('Starting background process...')
    subprocess.Popen(CMD.format(FILE))
    print('Background process started. Waiting for 10 seconds...')
    time.sleep(10)
    print('Stopping parent process...')


if __name__ == '__main__':
    main()
