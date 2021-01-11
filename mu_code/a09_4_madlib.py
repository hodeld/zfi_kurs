#! python3
# 9_4_madlibs.py <filename> - reads <filename> and replaces any occurrences of
# 'ADJECTIVE', 'NOUN', 'ADVERB', 'VERB'.

import pyinputplus as pyip
import re
from pathlib import Path

keywords = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
p = Path.cwd().parent
folder_name = 'files'
file_name = 'madlibs.txt'
folder_path = p / folder_name
p = folder_path / file_name


if p.is_file():
    with open(p) as txtfile:
        txt = txtfile.read()

    for keyword in keywords:
        while(keyword in txt):
            print(f'Found {keyword}')
            replacement = pyip.inputStr(f'Enter an {keyword.lower()}: ')
            txt = txt.replace(keyword, replacement, 1)

    print(txt)

    with open((folder_path / 'madlibs_subs.txt'), 'w') as newTxtfile:
        newTxtfile.write(txt)
