from openpyxl import load_workbook
import googlemaps
from Tkinter import *
import tkFileDialog
import tkMessageBox

Tk().withdraw()
in_file = tkFileDialog.askopenfilename()
out_file = tkFileDialog.askopenfilename()
#tkMessageBox.showerror("message", "words")

START_COL = 'K'
DEST_COL = 'F'
DIST_COL = 'N'
TIME_COL = 'O'
SHEET = 'MATRICE'
IN_FILE = '20211029_MATRICE_Rev.01.xlsx'
OUT_FILE = 'out.xlsx'
API_KEY = 'AIzaSyATpT-vZJyIpbFWCSe7Oc9RyKdTIv7AnjY'

gmaps = googlemaps.Client(key=API_KEY)

wb = load_workbook(filename = IN_FILE)
ws = wb.get_sheet_by_name(SHEET)

start_col = map(lambda v: v.value, ws[START_COL][1:])
dest_col = map(lambda v: v.value, ws[DEST_COL][1:])
dist_col = ws[DIST_COL][1:]
time_col = ws[TIME_COL][1:]

for start, dest, dist, time in zip(start_col, dest_col, dist_col, time_col):
    if start and dest and not dist.value and not time.value:
        res = gmaps.distance_matrix(start, dest)
        print(res)
        exit(0)
        dist.value = '#'

wb.save(filename = OUT_FILE)