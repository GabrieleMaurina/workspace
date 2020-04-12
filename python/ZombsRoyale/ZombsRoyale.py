from PIL.ImageGrab import grab
from win32api import SetCursorPos as mouse
import win32api, win32con, win32gui, pywintypes
from tkinter import *
from tkinter import messagebox as msg
from threading import Thread
from time import sleep as s
from time import time as t
from configparser import ConfigParser as Config
import os
import sys
import json
import keyboard
import asyncio

ZOMBS = 'zombs'
PRECISION_KEY = 'precision'
SIZE_KEY = 'size'
COLORS_KEY = 'colors'

running = False

precision = 0
size = 0

SKIN = (253, 200, 118)
colors = []
config_colors = []

def set_defaults():
	global precision, size, config_colors
	precision = 2
	size = 2
	config_colors = [SKIN]

set_defaults()

PRECISIONS = [50, 75, 100, 125]
SIZES = [0.4, 0.6, 0.8, 1]

r = Tk()
X_SIZE = r.winfo_screenwidth()
Y_SIZE = r.winfo_screenheight()
X_CENTER = X_SIZE // 2
Y_CENTER = Y_SIZE // 2

step = 0
step_x = 0
step_y = 0
outer = 0
inner = 0

CONFIG_PATH = os.path.join(os.getenv('APPDATA'), 'zombs_royale.ini')
config = Config()
config.read(CONFIG_PATH)
try:
	precision = int(config[ZOMBS][PRECISION_KEY])
	size = int(config[ZOMBS][SIZE_KEY])
	cs = list(map(lambda c:tuple(c), json.loads(config[ZOMBS][COLORS_KEY])))
	if len(cs):
		config_colors = cs
except:
	pass

f = Frame(r, highlightthickness=3)
f.pack(fill='both', expand=1)

fps = Label(f, width=2, height=1, font=('Arial Black', '15'))

menu = Frame(f)

precision_frame = Frame(menu, relief=RIDGE, borderwidth=1)
precision_frame.pack()
precision_label = Label(precision_frame, text='Precision')
precision_label.pack()
precision_scale = Scale(precision_frame, from_=1, to=4, orient=HORIZONTAL)
precision_scale.pack()

area_frame = Frame(menu, relief=RIDGE, borderwidth=1)
area_frame.pack()
area_label = Label(area_frame, text='Size')
area_label.pack()
size_scale = Scale(area_frame, from_=1, to=4, orient=HORIZONTAL)
size_scale.pack()

def save_config():
	global config
	config = Config()
	config[ZOMBS] = {}
	config[ZOMBS][PRECISION_KEY] = str(precision)
	config[ZOMBS][SIZE_KEY] = str(size)
	config[ZOMBS][COLORS_KEY] = json.dumps(colors)
	with open(CONFIG_PATH, 'w') as config_file:
		config.write(config_file)

colors_frame = Frame(menu, relief=RIDGE, borderwidth=1)
colors_frame.pack(fill=X)
Frame(colors_frame).pack()
color_buttons = {}

MSG = False
def remove_color(c, quick=False):
	global MSG
	MSG = True
	if quick or msg.askyesno('Remove color', 'Are you sure?'):
		colors.remove(c)
		color_buttons[c].pack_forget()
		del color_buttons[c]
		if not quick:
			save_config()
	MSG = False

def add_color(color, quick=False):
	if color not in colors and len(color) < 10:
		colors.append(color)
		button = Button(colors_frame, bg=('#%02x%02x%02x' % color), command=lambda c=color:remove_color(c))
		button.pack(fill=X)
		color_buttons[color] = button
		if not quick:
			save_config()

r1 = Tk()
r1.geometry('{}x{}+{}+{}'.format(X_SIZE, Y_SIZE, 0, 0))
r1.wm_attributes("-topmost", True)
r1.wm_attributes("-disabled", True)
r1.wm_attributes("-transparentcolor", "white")
r1.overrideredirect(True)
r1.lift()
canvas = Canvas(r1, width=X_SIZE, height=Y_SIZE, bg='white', highlightthickness=0)

hWindow = pywintypes.HANDLE(int(canvas.master.frame(), 16))
exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

canvas.pack()

def draw_dots():
	canvas.delete('all')
	for i in range(1 - outer, outer):
		for j in range(1 - outer, outer):
			if i >= inner or i <= -inner or j >= inner or j <= -inner:
				canvas.create_rectangle(X_CENTER + i * step, Y_CENTER + j * step, X_CENTER + i * step, Y_CENTER + j * step)

def settings(first=False, quick=False):
	global step, step_x, step_y, outer, inner
	step = Y_SIZE // PRECISIONS[precision]
	step_x = [-step, 0, step, 0]
	step_y = [0, step, 0, -step]
	outer = int(PRECISIONS[precision] * SIZES[size] / 2)
	inner = int(PRECISIONS[precision] * 0.04)
	if not quick:
		save_config()
	if first:
		r.after(10, draw_dots)
	else:
		draw_dots()

def set_config(first=False):
	precision_scale.set(precision + 1)
	size_scale.set(size + 1)
	settings(first=first, quick=True)
	for color in list(colors):
		remove_color(color, quick=True)
	for color in config_colors:
		add_color(color, quick=True)
	save_config()

set_config(first=True)

def update_precision(event=None):
	global precision
	precision = precision_scale.get() - 1
	settings()

precision_scale.config(command=update_precision)

def update_size(event=None):
	global size
	size = size_scale.get() - 1
	settings()

size_scale.config(command=update_size)

def set_pos(event=None):
	r.geometry('+{}+{}'.format(X_SIZE - r.winfo_width(), 0))

set_pos()

def set_pause(event=None):
	global running, MSG
	if not MSG:
		running = False
		f['highlightbackground'] = 'red'
		fps.pack_forget()
		r1.deiconify()
		menu.pack()

def set_run(event=None):
	global running, MSG
	if not MSG:
		running = True
		f['highlightbackground'] = 'green'
		fps.pack()
		r1.withdraw()
		menu.pack_forget()

async def screenshot():
	return grab()

loop = asyncio.get_event_loop()
task = loop.create_task(screenshot())

counter = 0
last = t()
async def find():
	global counter, last, task

	im = await task
	task = loop.create_task(screenshot())

	x = X_CENTER + inner * step
	y = Y_CENTER - inner * step

	for circle in range(inner, outer):
		for i in range(4):
			for j in range(circle * 2):

				x += step_x[i]
				y += step_y[i]

				if im.getpixel((x, y)) in colors:
					c = 1
					xC = x
					yC = y

					for i in range(inner + 1, inner + 2):
						xS = x + i * step
						for j in range(inner + 1, inner + 2):
							if i != 0 or j != 0:
								yS = y + j * step
								if im.getpixel((xS, yS)) in colors:
									c += 1
									xC += xS
									yC += yS
					xC //= c
					yC //= c
					mouse((xC, yC))
					counter += 1
					return
		x += step
		y -= step
	counter += 1

	time = t()
	delta = time - last
	if delta >= 1:
		fps['text'] = int(round(counter / delta))
		last = time
		counter = 0

def findT():
	while True:
		if running:
			loop.run_until_complete(find())
		else:
			s(0.1)

def get_new_color():
	add_color(grab().getpixel((r.winfo_pointerx(), r.winfo_pointery())))

def pause():
	if running:
		set_pause()
	else:
		set_run()

enter_key = False
def handle_pause():
	global enter_key
	pressed = keyboard.is_pressed('\n')
	if not enter_key and pressed:
		enter_key = True
		r.after(1, pause)
	if enter_key and not pressed:
		enter_key = False

c_key = False
def handle_color():
	global c_key
	pressed = keyboard.is_pressed('c')
	if not c_key and pressed:
		c_key = True
		get_new_color()
	if c_key and not pressed:
		c_key = False

def utilities():
	handle_color()
	handle_pause()
	r.after(10, utilities)

def key(event=None):
	if event.char == 'c':
		get_new_color()
	elif event.char == 'r':
		global MSG
		MSG = True
		if msg.askyesno('Reset settings', 'Are you sure?'):
			set_defaults()
			set_config()
		MSG = False

r.overrideredirect(True)
r.attributes("-topmost", True)
r.bind('<Escape>', sys.exit)
r.bind('<Key>', key)
r.bind('<FocusIn>', set_pause)
r.bind('<FocusOut>', set_run)
r.bind('<Configure>', set_pos)

findThread = Thread(target=findT, daemon=True)
findThread.start()

set_run()
r.after(10, utilities)
r.mainloop()