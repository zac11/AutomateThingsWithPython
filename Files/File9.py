import os

"""
Open a file and write in it
"""

baconFile=open('/home/zac/Downloads/bacon','w')
baconFile.write('Hello World!\n')
baconFile.close()

baconFile=open('/home/zac/Downloads/bacon','a')
baconFile.write('Pizza is love, Pizza is life')
baconFile.close()

baconFile=open('/home/zac/Downloads/bacon')
baconContent =baconFile.read()
baconFile.close()
print(baconContent)


