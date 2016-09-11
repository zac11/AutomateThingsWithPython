import re

"""
This is an example of a greedy regex
"""
greedyregex=re.compile(r'(Ha){3,5}')
mo1=greedyregex.search('HaHaHaHaHa')
print(mo1.group())


"""
This is an example of a non greedy regex
"""
nongreedyregex=re.compile(r'(Ha){3,5}?')
mo2=nongreedyregex.search('HaHaHaHaHa')
print(mo2.group())

