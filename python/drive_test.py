import requests

url = 'https://drive.google.com/uc?export=download&id=13xal4Bf-IGb4Box0pHh7lFaQ98XAxkrHEegMx6To_BQ'
r = requests.get(url,allow_redirects=True)

open('test.docs','wb').write(r.content)
