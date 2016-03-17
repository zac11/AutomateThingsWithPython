listofcricket=['kohli','mathews','morgan','southee','tamim','smith']

print('Enter a name to search')
name = input()

if name not in listofcricket:
    print(name+' is not in the list of cricketers')
else:
    print(name+' is in this list')
