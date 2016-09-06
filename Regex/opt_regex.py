#we can match optional patterns using the ? character
import re

batregex=re.compile(r'Bat(wo)?man')
mo=batregex.search('Batman is good')
print(mo.group())

mo2=batregex.search('The adventures of Batwoman')
print(mo2.group())

#the (wo)? means that pattern is an optional one

phoneregex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3=phoneregex.search('The number is 783-688-5839')
print(mo3.group())