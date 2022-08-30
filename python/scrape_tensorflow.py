from os.path import join
from os import walk
from withcd import cd
from re import compile as re_cmp

PATH = join('tensorflow', 'tensorflow', 'python')

FROM = re_cmp(r'from (\S+) import')

def main():
    with cd(PATH):
        for root, dirs, files in walk('.'):
            for f in files:
                if f.endswith('.py'):
                    with open(join(root, f), 'r', encoding='utf-8') as f:
                        f = f.read()
                    for match in FROM.findall(f):
                        if match.startswith('tensorflow') and not match.startswith('tensorflow.python'):
                            print(match)

if __name__ == '__main__':
    main()