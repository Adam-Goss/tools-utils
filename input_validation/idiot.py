#! python3

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours: '
    res = pyip.inputYesNo(prompt)

    if res == 'no':
        break

print('Thank you. Have a nice day.')
