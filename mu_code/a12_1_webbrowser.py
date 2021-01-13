import webbrowser
import requests
from pathlib import Path

url = 'https://inventwithpython.com/'
url = 'https://www.vtg.admin.ch/de/einsatzmittel/boden-luft/panzerjaeger.html'
#webbrowser.open(url)

#in shell
#import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
cwd = Path.cwd()
file_folder = cwd.parent / 'files'
#res.json() res.text
res.content()
with open(file_folder / 'RomeoAndJuliet.txt', 'wb') as playFile:   # binary
        for chunk in res.iter_content(100000):
                playFile.write(chunk)


