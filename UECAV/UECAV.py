DEPLOYMENT = False
VERSION = '1.2'

logged = False
session = None

URL_API = 'http://vignale.openarchaeology.eu/w/api.php'
URL_PAGES = 'http://vignale.openarchaeology.eu/wiki/'
USERNAME = 'maurina'
PASSWORD = 'gabriele'

responses = 0
tot = 0
negatives = []
tsv = []
working = 0

WIDTH = 400
HEIGHT = 350

H = 'H'
ACTIVITY = 39
DEFINITION = 12
DESCRIPTION = 21

CONSTANT_VALUES = [(1, 'Vignale'), (45, 'Enrico Zanini')]

DB_COLUMNS = ['us', 'località', 'anno', 'area', 'saggio', 'ambiente', 'quota max', 'quota min', 'sezioni',
			'prospetti', 'foto', 'tabelle materiali', 'definizione', 'criteri distinzione', 'modo formazione',
			'componenti inorganiche', 'componenti organiche', 'consistenza', 'colore', 'misure', 'stato conservazione',
			'descrizione', 'uguale a', 'si lega a', 'gli si appoggia', 'coperto da', 'tagliato da', 'riempito da',
			'si appoggia a', 'copre', 'taglia', 'riempie', 'anteriore a', 'posteriore a', 'osservazioni', 'interpretazione',
			'elementi datanti', 'datazione', 'periodo', 'attività', 'campionatura', 'flottazione', 'setacciatura',
			'affidabilità', 'compilatore', 'responsabile']





from tkinter import *
import tkinter.ttk as ttk
import requests
import json
import re
from PIL import Image, ImageTk
import sys
from time import gmtime, strftime





def fetchIntList(linesIter):
	l = ''
	try:
		l = next(linesIter)
		l = re.sub('[^0-9,]+', '', l)
		l = re.sub(',', ', ', l)
		if not re.match('([0-9]+, )*[0-9]+', l):
			l = ''
	except:
		pass
	
	return l

def fetchYear(linesIter):
	l = ''
	try:
		l = next(linesIter)
		l = re.findall('[0-9]{4}', l)
		if l and len(l) == 0:
			l = l[0]
		else:
			l = ''
	except:
		pass
	
	return l

def fetchDescription(linesIter):
	l = ''
	d = ''
	
	try:
		while(l != H):
			d += l
			l = next(linesIter)
	except:
		pass
	
	return d

def fetchActivity(txt):
	activity = re.findall('Attività [0-9]+', txt)
	
	if activity:
		activity = re.sub('[^0-9]+', '', activity[0])
	
	return activity

KEYS = {'ambiente': (fetchIntList, 5), 'area': (fetchIntList, 3), 'sondaggio': (fetchIntList, 4),
		'data di scavo': (fetchYear, 2), 'da uomini e cose a vignale.': (fetchDescription, 12), 'descrizione': (fetchDescription, 21),
		'uguale a': (fetchIntList, 22), 'si lega a': (fetchIntList, 23), 'gli si appoggia': (fetchIntList, 24),
		'coperto da': (fetchIntList, 25), 'tagliato da': (fetchIntList, 26), 'riempito da': (fetchIntList, 27),
		'si appoggia a': (fetchIntList, 28), 'copre': (fetchIntList, 29), 'taglia': (fetchIntList, 30),
		'riempie': (fetchIntList, 31)}

def showProgress(uses):
	progressFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
	progress['value'] = 0
	number['text'] = 'Scaricamento ' + str(uses) + ' US.'
	results.place_forget()
	settings.place_forget()
	
	root.update()

def showEnd(negatives):
	global working
	
	results.place(relx=0.5, rely=0.5, anchor=CENTER)
	settings.place_forget()
	progressFrame.place_forget()
	
	nf = len(negatives)
	f = tot - nf
	
	if f > 0:
		success['text'] = str(f) + '/' + str(tot) + ' US scaricat' + ('e' if f > 1 else 'a') + '.'
		
		success.grid(row=0, column=1, sticky=W)
		successImage.grid(row=0, column=0, padx=(0, 10))
	else:
		success.grid_forget()
		successImage.grid_forget()
	
	if nf > 0:
		txt = str(nf) + '/' + str(tot) + ' US non trovat' + ('e' if nf > 1 else 'a') + '. '
		
		MAX = 3
		neg = [str(n) for n in negatives[:MAX]]
		txt += '(' + ', '.join(neg)
		if tot > MAX:
			txt += '...'
		txt += ')'
		
		notFound['text'] = txt
		
		notFound.grid(row=1, column=1, sticky=W)
		notFoundImage.grid(row=1, column=0, padx=(0, 10))
	else:
		notFound.grid_forget()
		notFoundImage.grid_forget()
	
	root.update()
	
	working = 2

def showSettings():
	global working

	settings.place(relx=0.5, rely=0.5, anchor=CENTER)
	results.place_forget()
	progressFrame.place_forget()
	us.focus_set()
	
	root.update()
	
	working = 0

def resource_path(relative):
	if DEPLOYMENT:
		if hasattr(sys, "_MEIPASS"):
			return os.path.join(sys._MEIPASS, relative)
		return os.path.join(relative)
	else:
		return relative

def err(text='Error', color='red'):
	error['text'] = text
	error['fg'] = color

def login():
	global logged
	global session
	
	try:
		session = requests.session()
		
		par = {'action':'login', 'lgname':USERNAME, 'format':'json'}
		res = json.loads(session.post(URL_API, params=par).text)
		
		par = {'action':'login', 'lgname':USERNAME, 'lgpassword':PASSWORD, 'format':'json', 'lgtoken':res['login']['token']}
		res = json.loads(session.post(URL_API, data=par).text)
		
		logged = res['login']['result'] == 'Success'
	except:
		pass
	
	if(not logged):
		err('Impossibile connettersi al server.')

def getResults(us, p):
	txt = p.text
	
	pos = txt.find('</head>')
	if pos > -1:
		txt = txt[pos + 6:]
	
	a = fetchActivity(txt)
	
	txt = re.sub('<div class="printfooter">(.|\n)*', '', txt)
	txt = re.sub('<!--(.|\n)*?-->', '', txt)
	txt = re.sub('<script>(.|\n)*?<\/script>', '', txt)
	txt = re.sub('<style>(.|\n)*?<\/style>', '', txt)
	txt = re.sub('<h([0-9]|(r \/))>', '\n' + H + '\n', txt)
	txt = re.sub('<(?!<).*?>', '', txt)
	txt = re.sub('\[modifica\]', '', txt)
	txt = re.sub('\t', '', txt)
	txt = re.sub('\n{2,}', '\n', txt)
	txt = re.sub('Vai a:navigazione, ricerca', '', txt)
	txt = txt.strip()
	
	lines = iter([l.strip() for l in txt.splitlines()])

	r = [''] * len(DB_COLUMNS)
	r[DB_COLUMNS.index('us')] = str(us).zfill(4)
	
	if a:
		r[ACTIVITY] = a
	
	for C in CONSTANT_VALUES:
		r[C[0]] = C[1]
	
	keys = KEYS.copy()
	
	for l in lines:
		k = keys.pop(l.lower(), None)
		if k:
			r[k[1]] = k[0](lines)
	
	if r[DEFINITION] == '' and r[DESCRIPTION] != '':
		r[DEFINITION] = r[DESCRIPTION]
	elif r[DESCRIPTION] == '' and r[DEFINITION] != '':
		r[DESCRIPTION] = r[DEFINITION]
	
	return r

def saveResults(tsv):
	if len(tsv):
		out = open('UECAV ' + strftime("%Y-%m-%d %H-%M-%S", gmtime()) + '.tsv', 'w', encoding='utf8')

		out.write('\t'.join(DB_COLUMNS) + '\n')
		for v in tsv:
			out.write('\t'.join(v) + '\n')
		
		out.close()

def find(usesIter):
	global responses
	global negatives
	global tsv
	
	if working == 1:
		try:
			us = next(usesIter)

			p = session.post(URL_PAGES + 'US_' + str(us).zfill(4))
			
			if p.status_code == 200:
				tsv.append(getResults(us, p))
			else:
				negatives.append(us)
			
			responses += 1
			progress['value'] = responses / tot * 100
			root.update()
			
			root.after(1, lambda : find(usesIter))
			
		except:
			saveResults(tsv)
			root.after(30, lambda : showEnd(negatives))

def fetch(uses):
	global responses
	global tot
	global negatives
	global tsv
	
	uses = list(uses)
	
	responses = 0
	tot = len(uses)
	negatives = []
	tsv = []
	
	usesIter = iter(uses)
	
	root.after(1, lambda : find(usesIter))

def getUses(us):
	try:
		uses = set()
		for u in us.split(','):
			sides = u.split('-')
			l = len(sides)
			if l == 0 or l > 2:
				raise Exception()
			elif l == 1:
				i = int(sides[0])
				uses.add(i)
			elif l == 2:
				min = int(sides[0])
				max = int(sides[1])
				for n in range(min, max + 1):
					uses.add(n)
		if len(uses) == 0:
			raise Exception()
		return uses
	except:
		err('Sintassi selezione US non valida')
		return None

def export():
	global working
	
	if working == 0:
		working = 1
		login()
		if(not logged):
			working = 0
			return;
		
		uses = getUses(us.get())
		if uses != None:
			showProgress(len(uses))
			fetch(uses)
		else:
			working = 0

def exportAsync():
	root.after(1, export)
	
def enterHandler(event):
	if working == 0:
		exportAsync()
	elif working == 1:
		showSettings()
	elif working == 2:
		showSettings()

def escHandler(event):
	sys.exit()





root = Tk()
root.title('UECAV  -  V ' + VERSION)
root.iconbitmap(resource_path('Icon.ico'))





frameTitle = Frame(root, relief=RIDGE, borderwidth=2)
frameTitle.pack(side=TOP, anchor=N, fill=X, padx=(10, 10), pady=(10, 10))

title = Label(frameTitle, text='Uomini e Cose a Vignale', font=(None, 20))
title.pack(side=TOP, pady=(10, 10))





border = Frame(root, relief=RIDGE, borderwidth=2)
border.pack(side=TOP, anchor=N, fill=BOTH, expand=True, padx=(10, 10), pady=(0, 10))

main = Frame(border)
main.pack(side=TOP, anchor=N, fill=BOTH, expand=True, padx=(10, 10), pady=(10, 10))





settings = Frame(main)

gridFrame = Frame(settings)
gridFrame.pack(side=TOP, anchor=N)

usLabel = Label(gridFrame, text='US (es. 1, 2, 5-7)', font=(None, 10))
usLabel.grid(row=0, column=0, padx=(0, 10))

us = Entry(gridFrame, width=30)
us.grid(row=0, column=1)

downloadButton = Button(settings, text="Scarica", font=(None, 20), command=exportAsync)
downloadButton.pack(side=TOP, anchor=N, pady=(30, 0))

error = Label(settings, text='', font=(None, 10))
error.pack(side=TOP, anchor=N, pady=(30, 0))




progressFrame = Frame(main)

number = Label(progressFrame, font=(None, 10), text='Scaricamento n US')
number.pack(side=TOP, anchor=N)

progress = ttk.Progressbar(progressFrame, orient=HORIZONTAL, length=300, mode='determinate')
progress.pack(side=TOP, anchor=N, pady=(30, 0))

interrupt = Button(progressFrame, text="Interrompi", font=(None, 20), command=showSettings)
interrupt.pack(side=TOP, anchor=N, pady=(30, 0))




results = Frame(main)

resultsGrid = Frame(results)
resultsGrid.pack(side=TOP, anchor=N)

successPhoto = ImageTk.PhotoImage(Image.open(resource_path('Tick.png')))
successImage = Label(resultsGrid, image=successPhoto)
successImage.image = successPhoto
successImage.grid(row=0, column=0)

success = Label(resultsGrid, font=(None, 10), text='')
success.grid(row=0, column=1)

notFoundPhoto = ImageTk.PhotoImage(Image.open(resource_path('Cross.png')))
notFoundImage = Label(resultsGrid, image=notFoundPhoto)
notFoundImage.image = notFoundPhoto
notFoundImage.grid(row=1, column=0)

notFound = Label(resultsGrid, font=(None, 10), text='')
notFound.grid(row=1, column=1)

endButton = Button(results, text="Fine", font=(None, 20), command=showSettings)
endButton.pack(side=TOP, anchor=N, pady=(30, 0))




showSettings()
x = (root.winfo_screenwidth() // 2) - (WIDTH // 2)
y = (root.winfo_screenheight() // 2) - (HEIGHT // 2) - 100
root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))
root.bind('<Return>', enterHandler)
root.bind('<Escape>', escHandler)




root.mainloop()