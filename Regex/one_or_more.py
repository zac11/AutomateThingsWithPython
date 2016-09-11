import re
batregex=re.compile(r'Bat(wo)*man')
mo1=batregex.search('The adventures of Batman')
print(mo1.group())

mo2=batregex.search('The adventures of Batwoman')
print(mo2.group())

mo3=batregex.search('The adventures of Batwowowowowowowoman')
print(mo3.group())

batregex1=re.compile(r'Bat(wo)+man')
mo4=batregex1.search('The adventures of Batwoman')
print(mo4.group())

mo5=batregex1.search('The adventures of Batwowowoman')
print(mo5.group())

mo6=batregex1.search('The adventures of Batman')
print(mo6==None)
