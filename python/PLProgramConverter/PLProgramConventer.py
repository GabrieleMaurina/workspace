from tkinter import *
from re import compile, IGNORECASE
from configparser import ConfigParser as Config
import os

SQUAT_STRINGS = ['squat']
BENCH_PRESS_STRINGS = ['bench press', 'benchpress', 'panca']
DEADLIFT_STRINGS = ['deadlift', 'stacco']

SQUAT_KEY = 'squat'
BENCH_PRESS_KEY = 'bench press'
DEADLIFT_KEY = 'deadlift'
RM1_KEY = '1RM'

CONFIG_PATH = os.path.join(os.getenv('APPDATA'), 'PLProgramConverter.ini')

r = Tk()
X_SCREEN = r.winfo_screenwidth()
Y_SCREEN = r.winfo_screenheight()

rm1_frame = Frame(r, relief=RIDGE, bd=2)
rm1_frame.pack(padx=10, pady=10, fill=X)

rm1 = Label(rm1_frame, text='1RM', font=('Arial', '25'))
rm1.pack()

config = Config()
config.read(CONFIG_PATH)

values_frame = Frame(rm1_frame)
values_frame.pack()

label_squat = Label(values_frame, text='Squat:', font=('Arial', '15'))
label_squat.pack(side=LEFT, padx=(5, 0))
squat = Entry(values_frame, validate=ALL)
squat.pack(side=LEFT, padx=(10, 50))
try:
	value = int(config[RM1_KEY][SQUAT_KEY])
	squat.delete(0, END)
	squat.insert(0, value)
except:
	pass

label_bench_press = Label(values_frame, text='Bench press:', font=('Arial', '15'))
label_bench_press.pack(side=LEFT)
bench_press = Entry(values_frame, validate=ALL)
bench_press.pack(side=LEFT, padx=(10, 50))
try:
	value = int(config[RM1_KEY][BENCH_PRESS_KEY])
	bench_press.delete(0, END)
	bench_press.insert(0, value)
except:
	pass

label_deadlift = Label(values_frame, text='Deadlift:', font=('Arial', '15'))
label_deadlift.pack(side=LEFT)
deadlift = Entry(values_frame, validate=ALL)
deadlift.pack(side=LEFT, padx=(10, 10))
try:
	value = int(config[RM1_KEY][DEADLIFT_KEY])
	deadlift.delete(0, END)
	deadlift.insert(0, value)
except:
	pass

def save_config():
	global config
	config = Config()
	config[RM1_KEY] = {}
	config[RM1_KEY][SQUAT_KEY] = squat.get()
	config[RM1_KEY][BENCH_PRESS_KEY] = bench_press.get()
	config[RM1_KEY][DEADLIFT_KEY] = deadlift.get()
	with open(CONFIG_PATH, 'w') as config_file:
		config.write(config_file)

save = None
numbers_only = compile('[0-9]*')
def validate(string):
	global save
	if numbers_only.fullmatch(string):
		if save:
			r.after_cancel(save)
		save = r.after(500, save_config)
		return True
	else:
		return False
vcmd = (r.register(validate), '%P')

squat['vcmd'] = vcmd
bench_press['vcmd'] = vcmd
deadlift['vcmd'] = vcmd

program_frame = Frame(r, relief=RIDGE, bd=2)
program_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

program = Text(program_frame, height=20, width=50, font=('Arial', '10'))
program.pack(padx=10, pady=10, fill=BOTH, expand=True)
program.focus_set()

percentage = compile('[0-9]{1,3}%')
excercise = compile('|'.join(SQUAT_STRINGS + BENCH_PRESS_STRINGS + DEADLIFT_STRINGS), IGNORECASE)
def convert():
	text = program.get(1., END)
	rm1 = 0
	pos = 0
	scanning = True
	while scanning:
		per = percentage.search(text, pos)
		if per:
			posend = per.span()[1]
			per = float(per.group().replace('%', '')) / 100
			ex = list(excercise.finditer(text, pos, posend))
			if len(ex):
				ex = ex[-1].group().lower()
				if ex in SQUAT_STRINGS:
					rm1 = int(squat.get())
				elif ex in BENCH_PRESS_STRINGS:
					rm1 = int(bench_press.get())
				elif ex in DEADLIFT_STRINGS:
					rm1 = int(deadlift.get())

			value = round(per * rm1, 1)
			if value.is_integer():
				value = int(value)
			value = str(value)

			text = text[:posend] + ' ' + value + 'Kg' + text[posend:]
			pos = posend
		else:
			scanning = False
	program.delete(1.0, END)
	program.insert(END, text)

convert_button = Button(program_frame, text='Convert', font=('Arial', '15'), command=convert)
convert_button.pack(side=BOTTOM, pady=10)

r.update_idletasks()
r.geometry('+{}+{}'.format((X_SCREEN - r.winfo_width()) // 2, (Y_SCREEN - r.winfo_height()) // 2 - 200))
r.title('PLProgramConverter')
r.mainloop()