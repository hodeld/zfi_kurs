import webbrowser
import requests
from pathlib import Path
import bs4

url = 'https://www.vtg.admin.ch/de/einsatzmittel/boden-luft/panzerjaeger.html'

res = requests.get(url)
res.raise_for_status()  #stops
if res.ok:
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

imgs = soup.select('img')
author = soup.select('#author')

for d in imgs:
    print(d)



#2.


