while True:
    print('Please enter the age ')
    age=input()
    if age.isdecimal():
        break
    else:
        print('Please enter a valid age')



while True:
    print('Please enter the password')
    passwd=input()
    if passwd.isalnum():
        break
    else:
        print('Please enter a valid password')