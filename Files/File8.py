import os

"""
Opening a file and reading
"""

hellofile=open('/home/zac/Downloads/Pug')

helloContent = hellofile.read()

print(helloContent)


"""
Printing strings divided by line breaks
"""

hellonewFile=open('/home/zac/Downloads/Poet')

hellonewContent = hellonewFile.readlines()

print(hellonewContent)