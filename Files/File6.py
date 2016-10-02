import os


"""
Lists all the directories
"""

print(os.listdir('/home/zac/Downloads'))

"""
Getting the size of the filename in bytes
"""
print(os.path.getsize('/home/zac/Downloads/PyPy/Automate Things With Python.pdf'))



"""
Getting total size of the Downloads folder
"""
totalfilesize=0
for filename in os.listdir('/home/zac/Downloads'):
    totalfilesize=totalfilesize+os.path.getsize(os.path.join('/home/zac/Downloads',filename))
print(totalfilesize)