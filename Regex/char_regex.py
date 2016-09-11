import re
christregex=re.compile(r'\d+\s\w+')

"""
The regular expression defined by christregex will match text with
1 or more numeric text - \d+
one or more whitespace character - \s
one or more letter/digit/underscore character - \w+

"""
mo1=christregex.findall('12 drummers ,11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, '
                   '5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo1)



willywonka =re.compile('\w+\s')

"""
The regular expression defined by willywonka will match text with
1 or more numeric text - \d+
one or more whitespace character - \s
"""
mo2=willywonka.findall('So far, the latest is Eclipse Kepler (4.3.2). '
                       'You can follow below steps to install it on Ubuntu 14.04 or other Ubuntu releases.')

print(mo2)