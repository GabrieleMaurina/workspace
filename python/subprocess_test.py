import subprocess
import sys
import time


def parent():
    for i in range(3):
        print('parent:', i)
        time.sleep(1)


def child():
    for i in range(10):
        print('child:', i)
        time.sleep(1)


def main():
    if sys.argv[1] == 'parent':
        subprocess.Popen(['python', 'subprocess_test.py',
                         'child'], start_new_session=True)
        parent()
    elif sys.argv[1] == 'child':
        child()
    exit()


if __name__ == '__main__':
    main()
