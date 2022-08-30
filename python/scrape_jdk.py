from os.path import join
from os import walk
from withcd import cd
from re import compile as re_cmp

PATH = join('jdk', 'src')

NATIVE = re_cmp(r'native')

def main():
    with cd(PATH):
        for root, dirs, files in walk('.'):
            for f in files:
                if f.endswith('.java'):
                    with open(join(root, f), 'r', encoding='utf-8') as code:
                        code = code.read()
                    if NATIVE.search(code):
                        print(join(root, f))

if __name__ == '__main__':
    main()