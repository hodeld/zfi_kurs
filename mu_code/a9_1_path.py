from pathlib import Path
import os
cwd = Path.cwd()
newfolder_path = cwd / 'new'

try:
    os.makedirs(newfolder_path)  # create folder
except FileExistsError:
    pass

Path(newfolder_path).exists()

newfolder_path.is_absolute()

fname = 'newfile2.txt'
fpath = Path(newfolder_path, fname)
with open(fpath, 'w') as f:
    f.write('asdf')

