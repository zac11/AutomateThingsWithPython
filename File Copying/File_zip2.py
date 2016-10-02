import os,zipfile

"""
Extracting zip files in the current working directory
"""

os.chdir('/home/zac/Documents')

exampleFile = zipfile.ZipFile('Test_Dup.zip')

#extract all files
exampleFile.extractall()


#extract specific files

exampleFile.extract('Test_Dup/log.txt','/home/zac/Downloads/PyPy')


exampleFile.close()