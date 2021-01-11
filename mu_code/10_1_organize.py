import shutil
from pathlib import Path
import os

# copy a file
cwd = Path.cwd()
parent = cwd.parent
from_copy = parent / 'files'
to_copy = parent / 'files_backup'
try:
    os.mkdir(to_copy)
except FileExistsError:
    pass

to_copy_fname = to_copy / 'madlibs_copy.txt'
from_f = from_copy / 'madlibs.txt'

#shutil.copy(from_f, to_copy)  # to_copy_fname
shutil.copy(from_f, to_copy_fname)

#move
shutil.move(str(to_copy_fname), str(from_copy))  # needs to a string

#copy tree
shutil.copytree(to_copy, to_copy / 'backup')

