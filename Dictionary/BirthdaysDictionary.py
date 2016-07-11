"""
This dictionary stores the birthday of people and you can add a new one if it not already present

"""

dicBirthday={'Barack-Obama':'June-1','Donald Trump':'July-14','Bernie-Sanders':'Aug-14','Hilary Clinton':'Nov-12','Gary Busi':'Jan-1'}

while True:
    print('Please enter a name to show birthday. Enter blank to exit')
    name=input()
    if name=='':
        break
    if name in dicBirthday:
        print('Birthday of '+name+' is on '+dicBirthday[name])

    else:
        print('The birthday information for '+name+' is not present. Please add it to dictionary')
        print('Please enter the birthday again')
        bday=input()
        dicBirthday[name]=bday
        print('Dictionary has been updated')
