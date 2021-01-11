'''
Chapter 10 Organizing Files

Insert Gaps

As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.

'''

# insertGaps.py - Inserts a gap in sequence of numbered files with the
# given prefix. It uses mostly the functions of fillingGaps. The renamed
# files are moved temporarily into a temp dir.
# Usage: python insertGaps.py rootDir filenamePrefix gapAt

import os, shutil, sys
from operator import itemgetter
from pathlib import Path
import mu_code.a10_2_fillingGaps as fg

if __name__ == "__main__":

    cwd = Path.cwd()
    parent = cwd.parent
    fo_path = parent / 'files' / 'fillinggaps'
    fprefix = 'file_'
    gapAt = 3 # wanted gap

    fileList = fg.findMatchingFiles(fo_path, fprefix)
    sortedFileList = sorted(fileList, key=itemgetter(int(2)))
    lengthIntLiteral = fg.getLongestIntLiteral(sortedFileList)

    tempDirPath = Path(os.path.join(fo_path, 'temp'))
    if(os.path.exists(tempDirPath)):
        tempDirPath.rmdir()

    tempDirPath.mkdir()

    # Move the renamed files into a temp-dir, so that they are not
    # overwritten by themselves.
    # xxx4.txt --> xxx5.txt --> xx6.txt
    fg.renameFiles(sortedFileList, lengthIntLiteral, os.path.join('temp/' + fprefix), gapAt=gapAt)
    # Move the files back to the original dir
    for fn in os.listdir(tempDirPath):
        shutil.move(os.path.join(tempDirPath, fn), fo_path)

    tempDirPath.rmdir()
