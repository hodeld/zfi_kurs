'''
Chapter 10 Organizing Files

Filling in the Gaps

Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the
numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.

'''

# fillingGaps.py - Renames all files with the given prefix in a dir,
# so there are no gaps in the numbering sequence. It checks where the
# sequence start and pads all files to the same length of leading zeros
# Usage: python fillingGaps.py rootDir filenamePrefix

import sys, os, re, shutil
from pathlib import Path
from operator import itemgetter
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def findMatchingFiles(rootDir, filenamePrefix):
    ''' Matches the files in the rootDir to the given prefix and
        returns a list with the Path, integer literal, the integer literal
        as int and the suffix of the filename.
    '''
    pattern = re.compile(r'(' + filenamePrefix + r')(\d+)(.*)')  # \d+ all integers
    gapFileList = []

    for filename in os.listdir(rootDir):
    #for fpath in rootDir.glob(filenamePrefix + '*.*'): # would need fnam
        mo = pattern.match(str(filename))
        if mo is not None:
            intLiteral = mo.group(2)
            fileSuffix = mo.group(3)
            gapFileList.append([rootDir / filename, intLiteral, int(intLiteral), fileSuffix])

    return gapFileList

def getLongestIntLiteral(sortedFileList):
    ''' Returns the size of the longest integer literal e.g. 0002 --> 4
        TODO: Maybe there is a shorter pythonic version
    '''

    lengthIntLiteral = 0
    for sortedFile in sortedFileList:
        if len(sortedFile[1]) > lengthIntLiteral:
            lengthIntLiteral = len(sortedFile[1])
    return lengthIntLiteral

def renameFiles(sortedFileList, lengthIntLiteral, filenamePrefix, gapAt=None):
    ''' Loops through every file in the list. If the number in
        the file name is not the next in the sequence or hasn't the right
        amount of leading zeros renames it.

    '''

    # Find out where the sequence begins
    start = sortedFileList[0][2]
    end = len(sortedFileList)

    if gapAt:
        file_nrs = list(range(start, gapAt)) + list(range(gapAt + 1, end + 2))
    else:
        file_nrs = list(range(start, end + 1))
    assert len(file_nrs) == len(sortedFileList)
    for i, gapFile in zip(file_nrs, sortedFileList):

            ''' Check if the index is not already the same as the number OR
                the length of the integer literal is not the length of the longest 
                integer literal in the list
            '''
            if (i is gapFile[2] and len(gapFile[1]) == lengthIntLiteral):
                continue
                # i:0{lengthNumber} pads the new number to the length of the longest int literal
            else:
                src = gapFile[0]
                dest = Path(os.path.dirname(gapFile[0])) / f'{filenamePrefix}{i:0{lengthIntLiteral}}{gapFile[3]}'
                logging.info(f'renaming {src.name} to {dest.name}')
                shutil.move(src, dest)


def create_files(folder_path, fprefix=''):
    file_nr = list(range(1, 21))
    remov_nr = 1
    file_end = '.txt'
    leading_zeroes = 3

    for filename in folder_path.glob('*' + file_end):  # removes all
        os.unlink(filename)
    for k in range(6): # remove x nrs
        remov_nr += random.randint(1, 3)
        file_nr.remove(remov_nr)

    for i in file_nr:

        fname = fprefix + str(i).zfill(leading_zeroes) + file_end
        fpath = folder_path / fname
        with open(fpath, 'w') as f:
            f.write('#'+ fname)


if __name__ == "__main__":
    # from sys:
    # Usage: python fillingGaps.py rootDir filenamePrefix gapAt

    # fo_path = Path(sys.argv[1])
    # fprefix = sys.argv[2]

    cwd = Path.cwd()
    parent = cwd.parent
    fo_path = parent / 'files' / 'fillinggaps'
    fprefix = 'file_'
    create_files(fo_path, fprefix)


    gapFileList = findMatchingFiles(fo_path, fprefix)

    # Sort the list of files by the number
    sortedFileList = sorted(gapFileList, key=itemgetter(int(2)))
    lengthIntLiteral = getLongestIntLiteral(sortedFileList)
    renameFiles(sortedFileList, lengthIntLiteral, fprefix)



