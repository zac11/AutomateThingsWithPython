import re

#Will match all the vowels in the following lines
vowelregex=re.compile(r'[aeiouAEIOU]')
mo1=vowelregex.findall('Lionel Messi is a best footballer ever. Bitch')
print(mo1)


#This will match all the other letters except the vowels
negatevowelregex=re.compile(r'[^aeiouAEIOU]')
mo4=negatevowelregex.findall('Lionel Messi is a best footballer ever. Bitch')
print(mo4)


#This will match any character/letter/digit from 0-9

newvowelregex=re.compile(r'[a-zA-Z0-9]')
mo2=newvowelregex.findall('This happens to be one of the most contradicting stories ever told. A father that'
                          'was gay and wanted his 1 and only 1 son to not turn gay')
print(mo2)


mo3=newvowelregex.findall('So far, the latest is Eclipse Kepler (4.3.2). '
                          'You can follow below steps to install it on Ubuntu 14.04 or other Ubuntu releases.')

print(mo3)



