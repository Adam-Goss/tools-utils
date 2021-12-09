#! python3
# strong_password.py - detects if a password is strong or not 
# strong password = 8 or more chars long, upper and lower case chars, and 1 or more digits


import re

def isStrong(user_passwd):
    # check length
    if len >= 8:
        # check contains 1 or more digits
        digitRegex = re.compile(r'[0-9]+')
        if digitRegex.search(user_passwd):
            # check 1 or more [a-z]
            lowercaseRegex= re.compile(r'[a-z]+')
            if lowercaseRegex.search(user_passwd):
                # check 1 or more [A-Z]
                uppercaseRegex= re.compile(r'[A-Z]+')
                if uppercaseRegex.search(user_passwd):
                    return True

    return False


passwd = input('''Enter a strong password:
* Valid = 8 or more chars long, upper and lower case chars, and 1 or more digits
> '''
)

if isStrong(passwd):
    print(f'{passwd} is strong')
else:
    print(f'{passwd} is NOT strong')
