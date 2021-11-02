from shutil import rmtree
from string import ascii_letters,digits
from random import choices
from os import system, remove

key = ''.join(choices(ascii_letters+digits,k=16))

rmtree('dist',ignore_errors=True)
rmtree('build',ignore_errors=True)

cmd = []
cmd.append('pyinstaller')
cmd.append('-F')
cmd.append('-w')
cmd.append('-n ExcelMaps')
cmd.append('--icon=icon.ico')
cmd.append(f'--key={key}')
cmd.append('.excelmaps.py')

system(' '.join(cmd))

rmtree('build',ignore_errors=True)
try:
    remove('ExcelMaps.spec')
except FileNotFoundError:
    pass
