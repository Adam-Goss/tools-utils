#! python3
# date_detection.py - detects dates in DD/MM/YYYY format

import re

def isDate(date):
    dateRegex = re.compile(r'[0-3][0-9]/[0-2][0-9]/[1-2][0-9]{3}')
    # res = dateRegex.search(date)
    # print(res)
    # return res
    if dateRegex.search(date):
        return True
    else:
        return False

date = input('Enter a date:')

if isDate(date):
    print('Valid date')
else:
    print('Invalid date')
