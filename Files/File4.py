import os

"""
Prints the absolute path of argument
"""
print(os.path.abspath('.'))

"""
Prints absolute path of argument
"""

print(os.path.abspath('./log.txt'))

"""
Checks if path is absolute
"""

print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))