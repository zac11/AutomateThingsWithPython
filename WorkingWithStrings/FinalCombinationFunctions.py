decnum=123.4322
string_normal=' Welcome to Python Combination Program '
string_sel='Intro to Selenium WebDriver'

"""
Stripping whitespaces can be done by the strip() method
"""
print('Before stripping whitespaces string is '+string_normal)
print('After stripping whitespaces, string becomes '+string_normal.strip())

"""
Check whether Selenium text is present in the string_sel
"""

if 'Selenium' in string_sel:
    print('Selenium is present in '+string_sel)
else:
    print('Selenium is not present in '+string_sel)


"""
First string starts with Welcome, which can be checked using startswith() method
"""
if string_normal.startswith('Welcome'):
    print(string_normal+" starts with 'Welcome'")
else:
    print('First trim the whitespace and then try it again')
    print(string_normal.strip().startswith('Welcome'))
    print('Now it will match the starting point')

"""
Second string ends with Driver, which can be checked using endswith() method
"""

if string_sel.endswith('Driver'):
    print(string_sel+" string ended with 'Driver'")
else:
    print(string_sel+ "doesn't end with the checking string")


"""
Checking if the string is empty, which is done by isspace() method

"""

if string_sel.isspace():
    print('String is empty')
else:
    print('String is not empty')
"""
To check if the two strings are equal, we can simply use the == operator
"""

if string_sel=="Selenium WebDriver":
    print(string_sel+ " equals the text that we entered")
else:
    print(string_sel+ " doesn't equal the text that we entered")


"""
Priting the length of the string can be done by len(str) method
"""

print(len(string_normal))
print(len(string_sel))

"""
Replacing a portion of string can be done by replace() method
"""

print(string_normal.replace('Python','Angular',1))

"""
Converting the string to lowercase can be done by lower() method
"""

if string_normal.islower():
    print('String is already lower case')
else:
    print(string_normal.lower())

"""
Converting the string to uppercase can be done by upper() method
"""
if string_sel.isupper():
    print('String is already uppercase')
else:
    print(string_sel.upper())

"""
Splitting the string can be done by split() method
"""

print(string_normal.split())