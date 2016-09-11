import re
findallregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1=findallregex.search('This is his phone number : Cell : 783-688-5839 and Work : 012-422-3192')

"""
search() returns a match object on the first matched string pattern
"""
print(mo1.group())  #This will only print the Cell

"""
findall() returns a string on all matched pattern if there are no groups
"""
mo2=findallregex.findall("This is his phone number : Cell : 783-688-5839 and Work : 012-422-3192")
print(mo2) #This will return both Cell and Work



"""
findall() will return a tuple if the matched pattern has groups
"""

newregex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3=newregex.findall("This is his phone number : Cell : 783-688-5839 and Work : 012-422-3192")
print(mo3) #This will print a tuple