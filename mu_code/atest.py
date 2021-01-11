
from pathlib import Path
import shutil

p = Path.cwd()
file_end = 'py'
for txtFile in list(p.glob('*.' + file_end)):
    name = txtFile.name
    newname = 'a' + name
    shutil.move(txtFile, p / newname)
