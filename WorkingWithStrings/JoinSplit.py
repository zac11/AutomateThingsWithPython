"""
The join() method is called on a string value but passed a list value. It also returns a string value
"""


print('-'.join(['messi', 'andres', 'lionel']))

print(' '.join(['The', 'name', 'is', 'Bond!', 'James', 'Bond']))

print(' '.join(['I', 'want', 'to', 'slap', 'you']))


"""
The split() method is called on a string value, passed a string value, but returns a list value
"""

String1="Simon Cowell is a douche"
print(String1.split())

String2='Her#name#is#Rhonda#Rhimes'
print(String2.split('#'))

String3='Lexi Davis has a great ass'
print(String3.split('s'))

#Splitting a multi line string into single lines

String4="""
In La Liga 2016-17
Barcelona will
play without Messi,
and Andres Iniesta,
would be the main playmaker,
Luis Suarez would win the Pichichi.
EOS

"""

print(String4.split('\n'))
