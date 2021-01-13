'''
Chapter 12 Web Scraping

Image Site Downloader

Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that
has a search feature.
'''

# unsplashDl.py - Downloads all images on unsplash.com which are
# tagged with the searchterm
# USAGE: python unsplashDl.py searchterm
import logging, time, requests, re, sys
import bs4
from pathlib import Path

FILENAMEREGEX = r'(&dl=)(.*?)$'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_links_gesetze():
    base_url = 'https://www.google.com/search?tbm=isch&q='

    url = base_url + query
    url = 'https://www.admin.ch/gov/de/start/bundesrecht/systematische-sammlung.html'
    res = requests.get(url)
    res.raise_for_status()

    if res.ok:
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elemnts = soup.select('.clearfix a.icon--external ')

    cwd = Path.cwd()
    file_folder = cwd.parent / 'files'
    fname = 'gesetze.txt'
    fpath = file_folder / fname
    files = []
    for d in elemnts[:10]:
        f_link = d.get('href')
        fname_i = d.get_text()
        if f_link is None:
            continue
        files.append((fname_i, f_link))

    with open(fpath, mode='w') as textfile:
        for f in files:

            textfile.write(': '.join(f))
            textfile.write('\n\n')

if __name__ == "__main__":
    query = 'dog'
    get_links_gesetze()
