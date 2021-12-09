#! python3
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard
# usage: copy stuff to clipboard (Ctrl-A + Ctrl-C) then run script in terminal
# requires pyperclip is installed (pip install pyperclip)

import pyperclip, re

# regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?         # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)          # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)


# regex for email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot something (top-level domain)
)''', re.VERBOSE)

# get text from clipboard
text = str(pyperclip.paste())   
matches = []
# find all phone numbers
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
# find all email addresses
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:') 
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
