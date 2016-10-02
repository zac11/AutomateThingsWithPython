import os,zipfile

"""
Working with zip files using Python
"""

os.chdir('/home/zac/Documents')

#read a zip file using the zipfile module

exampleZip = zipfile.ZipFile('Test_Dup.zip')

#print the contents of the zip file
print(exampleZip.namelist())

#getting the information for the file within zip
zipInfo = exampleZip.getinfo('Test_Dup/log.txt')

#printing file size
print(zipInfo.file_size)

#printing file size post compress

print(zipInfo.compress_size)

print('Compressed file is %sx times smaller ! '%(round(zipInfo.file_size/zipInfo.compress_size,2)))


exampleZip.close()