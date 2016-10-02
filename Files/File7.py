import os

"""
Checks the validity of a filepath -> will return true if a file/folder exists
"""
print(os.path.exists('/home/zac/Downloads'))

print(os.path.exists('/home/zac/Downloads/shit'))



"""
Checks if the referred path is a file -> returns true if a file
"""
print(os.path.isfile('/home/zac/Downloads/log.txt'))

print(os.path.isfile('/home/zac/Downloads'))




"""
Checks if the referred path is a folder or directory -> returns true if a directory
"""

print(os.path.isdir('/home/zac/Downloads'))

print(os.path.isdir('/home/zac/Downloads/log.txt'))