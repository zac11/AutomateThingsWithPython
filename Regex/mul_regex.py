import re
heroregex=re.compile(r'Batman|Tina Fey')
mo1=heroregex.search('Batman and Tina Fey.')
print(mo1.group())

mo1=heroregex.search('Tina Fey and Batman')
print(mo1.group())

batregex=re.compile(r'Bat(man|mobile|copter|bat|bug)')
mo=batregex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))