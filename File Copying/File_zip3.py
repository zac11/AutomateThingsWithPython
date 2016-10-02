import zipfile,os

"""
Create a new zip file
"""

os.chdir('/home/zac/Documents')

newZip = zipfile.ZipFile('new_zip','w')

newZip.write('log.txt',compress_type=zipfile.ZIP_DEFLATED)

newZip.close()


