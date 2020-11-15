#!/usr/bin/env python

import sys
from PIL import Image, ImageDraw, ImageFont
import bisect
from functools import lru_cache
from random import randrange

print('Usage: python3 ascii_art.py <input> <output> <unicode limit> <char size> <density> <font> <multiplicity> <normilization>')

in_n=sys.argv[1] if len(sys.argv)>1 else 'input.png'
out_n=sys.argv[2] if len(sys.argv)>2 else 'output.png'
t=int(sys.argv[3]) if len(sys.argv)>3 else 127
s=int(sys.argv[4]) if len(sys.argv)>4 else 50
dns=float(sys.argv[5]) if len(sys.argv)>5 else 0.8
f=sys.argv[6] if len(sys.argv)>6 else '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
m=bool(sys.argv[7]) if len(sys.argv)>7 else False
n=bool(sys.argv[8]) if len(sys.argv)>8 else True

in_i=Image.open(in_n)
in_i=in_i.convert(mode='L')

colors={}
colors_keys=set()
for x in range(in_i.width):
    for y in range(in_i.height):
        colors_keys.add(in_i.getpixel((x,y)))

dlt=1/(len(colors_keys)-1)
new_col=0
for col in sorted(colors_keys):
    colors[col]=new_col if n else col/255
    new_col+=dlt

print('Generating table.')
font=ImageFont.truetype(f,s)
d={}
for ci in reversed(range(32,t)):
    c=chr(ci)
    i=Image.new('1', (s*2, s*2))
    dr=ImageDraw.Draw(i)
    dr.rectangle([0,0,s*2,s*2],fill=1)
    dr.text((s/2,s/2),c,font=font)
    key=0
    for x in range(s*2):
        for y in range(s*2):
            key+=i.getpixel((x,y))
    if m and key in d: d[key].append(c)
    else: d[key]=[c]
    print('\r'+str(int((t-ci)/t*100))+'%',end='')
print()
keys=sorted(d.keys())
d[keys[-1]]=[' ']
mn=keys[0]
dlt=keys[-1]-keys[0]
print('Table generated with {} keys.'.format(len(keys)))

def char(v):
    l=d[keys[nearest(v)]]
    return l[randrange(len(l))]

@lru_cache(maxsize=None)
def nearest(v):
    v=colors[v]*dlt+mn
    p=bisect.bisect_left(keys,v)
    if p>=len(keys): return p-1
    elif p==0: return 0;
    else: return p if abs(keys[p]-v)<abs(keys[p-1]-v) else p-1

print('Generating image.')
out_i=Image.new('1', (int(in_i.width*s*dns),int(in_i.height*s*dns)))
dr=ImageDraw.Draw(out_i)
dr.rectangle([0,0,out_i.width,out_i.width],fill=1)
for x in range(in_i.width):
    for y in range(in_i.height):
        dr.text((int(x*s*dns),int(y*s*dns)),char(in_i.getpixel((x,y))),font=font)
    print('\r'+str(int((x+1)/in_i.width*100))+'%',end='')
out_i.save(out_n)
print()
