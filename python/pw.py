from random import choices
from string import ascii_letters, digits, punctuation
from sys import argv

pool = ascii_letters + digits #+ punctuation
length = int(argv[1])

print(''.join(choices(pool, k=length)))

