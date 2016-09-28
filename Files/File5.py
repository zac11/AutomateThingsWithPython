import os
"""
Getting the base directory name and the directory name
"""

path='/home/zac/Pictures/Ghanta'

print((os.path.basename(path)))
print(os.path.dirname(path))


"""
Split a file path into basename and directory
"""
print(os.path.split(path))

"""
Separate components of the file path
"""
print(path.split(os.path.sep))