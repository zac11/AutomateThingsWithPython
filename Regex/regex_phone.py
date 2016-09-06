import re
#passing the desired pattern to compile() method
phonenumregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#calling the search method and then passing the required string on the phonenumregex
mo=phonenumregex.search('My number is 783-688-5839')
#mo contains the Match object and that can be used to print the matched object
print('Phone number found is '+mo.group())

#passed parameter searches for the braces
phonenumwithbraces=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1=phonenumwithbraces.search('The number is 783-688-5839')
print('Now this time the phone number is '+mo1.group())
#printing different groups in the regex
print(mo1.group(1))
print(mo1.group(2))
print(mo1.group(0))
print(mo1.groups())

#assigning area code and number to different groups from the tuple returned by groups()
areaCode,mainNumber=mo1.groups()
print(areaCode)
print(mainNumber)

#passed parameter already has an inbuilt braces.
phonewithbrackets=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2=phonewithbrackets.search('The number this time is (880) 099-8790')
print('The number this time is '+mo2.group())

