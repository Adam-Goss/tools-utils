#! python3 
# regex_strip.py - uses regex to implement the string strip() method
# if no arg given then whitespace at beginning/end is removed
# if arg give then this is removed from string

import re

def regexStrip(text, delimiter=""):
    if delimiter:
        stripRegex = re.compile(rf'{delimiter}')
        res = stripRegex.sub('', text)
        return res 
    else:
        stripRegex = re.compile(r'^\s+|\s+$')
        res = stripRegex.sub('', text)
        return res 

myString = "  Agent Alice gave the secret documents to Agent Bob"
print(myString)
newString = regexStrip(myString, "A")
print(newString)

