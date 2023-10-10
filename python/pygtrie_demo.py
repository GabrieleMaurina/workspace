from sys import argv
from pygtrie import StringTrie
from os import walk, sep
from os.path import join, normpath


def make_files_trie(path):
    trie = StringTrie(separator=sep)
    for root, dirs, files in walk(path):
        for file in files:
            file = normpath(join(root, file))
            trie[file] = file
    return trie


def main(path):
    trie = make_files_trie(path)

    # iterating all files
    for value in trie.itervalues():
        print(value)
    
    # iterating all files in folder
    for value in trie[r'pypi-packages\babelRTS-pypi':]:
        print(value)


if __name__ == '__main__':
    main(argv[1])
