from tkinter import *
from pyautogui import *
from time import sleep as s
import ctypes

SCREEN_X, SCREEN_Y = size()

WIDTH = 3
LENGTH = 3
DEPTH = 3
TURN = 602
VER = 250

pos = 0
depth = 0
running = True

def move_mouse(x=0, y=0):
	ctypes.windll.user32.mouse_event(1, x, y, 0, 0)

def turn_right():
	ctypes.windll.user32.mouse_event(1, TURN, 0, 0, 0)

def turn_left():
	ctypes.windll.user32.mouse_event(1, -TURN, 0, 0, 0)

def look_down():
	move_mouse(0, 1000)

def look_up():
	move_mouse(0, -600)

def key_pressed(e):
	print(e)

def set_pos(r):
	width = 100
	height = 100
	r.geometry('{}x{}+{}+{}'.format(width, height, SCREEN_X - width, 300))

r = Tk()
r.overrideredirect(True)
set_pos(r)
title = Label(r, text='7DTD - Bot')
title.pack()
f = Frame(r)
f.place(relx=0.5, rely=0.5, anchor=CENTER)
running_label = Label(f)
running_label.pack()

def dig_pillar():
	click()
	s(1.5)
	move_mouse(0, VER)
	s(0.1)
	click()
	s(1.5)
	move_mouse(0, -VER)
	s(0.1)

def dig():
	global pos
	global depth
	if running:
		dig_pillar()
		pos += 1

		t = pos // LENGTH
		k = pos % LENGTH
		print(pos)

		keyDown('w')
		if k == 0 or k == LENGTH - 1:
			s(0.6)
		else:
			s(0.35)
		keyUp('w')

		if t % 2 == 0:
			keyDown('d')
		else:
			keyDown('a')
		s(0.3)
		if t % 2 == 0:
			keyUp('d')
		else:
			keyUp('a')

		if k == 0:
			if t % 2 == 0:
				turn_left()
			else:
				turn_right()
		if k == LENGTH - 1:
			if t % 2 == 0:
				turn_right()
			else:
				turn_left()

		s(0.1)

		if depth < DEPTH - 1 and pos >= LENGTH * WIDTH - 1:
			pos = 0
			depth += 1

			turn_left()
			s(0.1)
			turn_left()
			s(0.1)
			turn_left()
			s(0.1)
			look_down()
			s(0.1)

			click()
			s(1.5)
			keyDown('s')
			keyDown('a')
			s(0.2)
			keyUp('s')
			keyUp('a')

			click()
			s(1.5)
			keyDown('s')
			keyDown('a')
			s(0.2)
			keyUp('s')
			keyUp('a')

			look_up()
			s(0.1)

	if depth < DEPTH - 1 or pos < LENGTH * WIDTH - 1:
		r.after(100, dig)

def set_running(event=None):
	global running
	if not running:
		running = True
		running_label['text'] = 'Running'
		running_label['fg'] = 'green'
		r.update_idletasks()
		click(SCREEN_X / 2, SCREEN_Y / 2)
		s(1)
		press('esc')
		r.after(1000, dig)

def set_paused():
	global running
	if running:
		running = False
		running_label['text'] = 'Paused'
		running_label['fg'] = 'red'
		r.update_idletasks()

set_paused()

def check_pause():
	if running and locateOnScreen('windows.png') is not None:
		set_paused()
	r.after(500, check_pause)

r.attributes("-topmost", True)
r.bind('<Return>', set_running)
r.bind('<Escape>', quit)
r.bind("<Key>", key_pressed)
r.after(500, check_pause)
r.mainloop()