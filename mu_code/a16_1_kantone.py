from pathlib import Path
import csv
import pprint
folder_p = '/Users/daim/softwareDev/21_smallstuff/21_zfiKurs/files'

fpath = Path(folder_p, 'kantone.csv')
f = open(fpath, 'r')
csv_file = csv.reader(f, delimiter=';')  # delimiter
csvdata = list(csv_file)
#pprint.pprint(csvdata)

kantone = {}
for sk_list in csvdata:
    #sk_list = sk[0].split(';')
    name = sk_list[0]
    hauptort = sk_list[-2]
    kantone[name] = hauptort
pprint.pprint(kantone)






