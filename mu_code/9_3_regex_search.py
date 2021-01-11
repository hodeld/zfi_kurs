'''
Chapter 9 Reading and Writing Files

Regex Search

Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.

'''

from pathlib import Path
import pyinputplus as pyip
import re

# evtl: Bug in pyip??? inputRegexStr calls validateRegex instead of validateRegexStr
#regex = pyip.inputRegexStr('Please input a regex: ')  # au
print('Enter eine regex')
regex = input()
pattern = re.compile(regex)

p = Path.cwd()
folder_name = 'quizes'
p = p / folder_name
file_end = 'txt'
for txtFile in list(p.glob('*.' + file_end)):
    with open(txtFile) as curFile:
        txtLines = curFile.readlines()
        for txtLine in txtLines:
            if(pattern.search(txtLine)):
                print(txtLine)