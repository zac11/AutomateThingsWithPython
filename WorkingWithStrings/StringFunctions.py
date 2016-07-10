spam="Hello World!"

"""
This will print uppercase
"""
print(spam.upper())

"""
This will print lowercase
"""
print(spam.lower())


"""
This will print a new string containing spam with lowercase
"""


spam1= spam.lower()
print(spam1)

"""
This will print a new string containing spam with uppercase
"""
spam2= spam.upper()
print(spam2)

"""This will see if the spam is in spam1 which shouldn't be
"""
print(spam in spam1)

"""
This will converted mixture of lowercase and uppercase input to lowercase and return answer
"""
print('How about your health')
feeling=input()
if feeling.lower()=='great':
    print("It's better than before")
else:
    print("No I am dying")

"""
This checks if spam is in all lowercase
"""
print(spam.islower())

"""
This checks if spam is in all uppercase
"""
print(spam.isupper())

"""
This checks if string is in uppercase
"""
print('HELLO'.isupper())

"""
This checks if string is in lowercase
"""
print('abcd1234'.islower())

"""
This checks if this string is lowercase
"""
print('12345'.islower())

"""
This checks if this string is uppercase"""
print('12345'.isupper())

"""
This will return true if string consists of only letters
"""
print('hello'.isalpha())

"""
This will return true if string consists of letters and numbers
"""
print('abcd1234'.isalnum())

"""
This will return true if the string contains numbers and not blank
"""
print('1234'.isdecimal())

"""
This will return true if the string contains space,tabs and not alphabets, numerics
"""
print('  '.isspace())

"""
This will return true if the string contains first uppercase letter followed by lowercase
"""
print('Hello'.istitle())


