def isPhoneNumber(text):
    """
        e.g. = 079-891-1111

        """
    if len(text) != 12:
         return False
    for i in range(0, 3):
        if not text[i].isdecimal():
             return False
    if text[3] != '-':
         return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

tel_nr = '079-891-1111'
print('Ist 079-891-1111 a phone number?')
print(isPhoneNumber('079-891-1111'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))


#2
import re

tel_nr_text = 'rufe an, wenn du Zeit hast: 079-891-1111. Danke. Ansonsten am Abend: 041-544-1234'
# backslash
re_tel_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # r: raw string
mo = re_tel_number.search(tel_nr_text) # matching object
mo.group()

#re_tel_number.findall(tel_nr_text) # list

#vowelRegex = re.compile(r'[aeiouAEIOU]')  # one of it
#vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

