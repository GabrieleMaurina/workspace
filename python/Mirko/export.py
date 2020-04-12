#testato con python3.8 su ubuntu 18.04

#importo librerie utili
from os import listdir #per ottenere la lista di file presenti in una cartella
from os.path import join as path #per manipolare perscorsi di file e cartelle
from re import search #per ricerca avanzata nel testo
from datetime import date #per operazioni con le date
from statistics import mean #per fare la media
from operator import itemgetter #per estrarre valori da una collection
from itertools import groupby #per raggruppare elementi in una lista

#nome della cartella contenente i file da analizzare
folder = 'Export Month'

#lista di stagioni, ogni stagione è una lista di mesi
seasonsMonths = [[1, 2, 12], [3, 4, 5],[6, 7, 8],[9, 10, 11]]

#periodo da filtrare
start = date(1993, 12, 1)
end = date(2014, 11, 1)

#lista dei file da analizzare
files = listdir(FOLDER)

with open('export.txt', 'w') as export: #apro il file export.txt in scrittura per salvare i risultati
	results = [] #preparo una lista coi risultati
	for name in files: #per ogni file nella cartella
		with open(path(folder, name), 'r', encoding='ISO-8859-1') as file: #apro il file
			content = file.read() #leggo il contenuto
			
			id = search(r'GRDC-No.:\s+.+', content).group().split()[1] #cerco il nome
			x = search(r'Latitude \(DD\):\s+.+', content).group().split()[2] #cerco la latitudine
			y = search(r'Longitude \(DD\):\s+.+', content).group().split()[2] #cerco la longitudine
			
			data = content.split('Flag\n')[1] #prendo la parte tabellare
			lines = [line.split(';') for line in data.split('\n') if line] #divido per righe ed ogni riga la divido per ";"
			dateAndCalculated = [[date.fromisoformat(line[0]), float(line[3].strip())] for line in lines] #tengo solo la data ed il valore
			period = [line for line in dateAndCalculated if line[0] >= start and line[0] <= end] #filtro sul periodo richiesto
			
			seasons = [[line for line in period if line[0].month in s] for s in seasonsMonths] #raggruppo i dati per stagione
			seasons = [[[line[0].year, line[1]] if line[0].month != 12 else [line[0].year + 1, line[1]] for line in s if line[1] >= 0] for s in seasons] #escludo i valori negativi
			seasons = [[[v[1] for v in g] for k, g in groupby(sorted(s), key=itemgetter(0))] for s in seasons] #raggruppo le stagioni per anno
			seasons = [[mean(year) for year in s if len(year) == 3]for s in seasons] #calcolo la media per ogni singola stagione
			seasons = [str(round(mean(s), 3)) if len(s) > 0 else '' for s in seasons] #calcolo la media tra tutte le stagioni escludendo quelle incomplete
			
			result = ';'.join([id, x, y] + seasons)	#compongo una riga del risultato concatenando valori e ";"
			results.append(result) #aggiungo il risultato alla lista dei risultati
	
		#ripeto per ogni file

	results = sorted(results) #ordino i risultati per ID
	results = '\n'.join(results) #combino tutti i risultati in un unica stringa
	export.write(results) #salvo nel file export.txt
