
from pathlib import Path
import shutil
import re
import os

p = Path.cwd()
file_end = 'py'
fprefix = 'a'

pattern = re.compile(r'(' + fprefix + r')(\d+)(_*.*.' + file_end + r')')

for filename in os.listdir(p):
    mo = pattern.match(str(filename))
    if mo is not None:
        nr = mo.group(2)
        rest = mo.group(3)
        newname = fprefix + str(nr).zfill(2) + rest
        shutil.move(p/ filename, p / newname)
