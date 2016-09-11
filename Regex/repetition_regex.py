import re
haregex=re.compile(r'(Ha){3}')
mo1=haregex.search('This is HaHaHa')
print(mo1.group())

mo2=haregex.search('This is Ha')
print(mo2==None)
