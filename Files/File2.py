"""
This program gets the current working directory.
"""

import os
print(os.getcwd())


os.chdir('/home/zac/Pictures')
print(os.getcwd())

"""
If the directory doesn't exits, then it will return error
"""

os.chdir('/home/zac/Dos')
print(os.getcwd())

"""
Traceback (most recent call last):
  File "/home/zac/PycharmProjects/AutomateThingsWithPython/Files/File2.py", line 16, in <module>
    os.chdir('/home/zac/Dos')
FileNotFoundError: [Errno 2] No such file or directory: '/home/zac/Dos'

"""

