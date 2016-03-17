namesoffoorballers=[]
#while condition since we want it to start from true and continue untill we end the condition
while True:

    print("Enter the names of footballers you know or press blank to stop")
    #enter the names of the footballers
    name = input()

    #if name is blank then break
    if name=='':
        break
    else:
        #else add to list name
        namesoffoorballers=namesoffoorballers + [name]
    print('Names of footballers')

    #print names of footballers
    for i in namesoffoorballers:
        print(''+i)
