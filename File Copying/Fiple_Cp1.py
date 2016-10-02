import os, shutil

"""
copying a file from one directory to another
"""

shutil.copy('/home/zac/Documents/Test/log.txt','/home/zac/Documents/Test2')


"""
copying file from one directory to another and give a new name
"""

shutil.copy('/home/zac/Documents/Test/log.txt','/home/zac/Documents/Test2/test.txt')



"""

Copy a whole directory into a new directory
"""
shutil.copytree('/home/zac/Documents/Test','/home/zac/Documents/Test_Dup')


"""
Removing the test file inside Test directory
"""

#os.unlink('/home/zac/Documents/Test2/test.txt')


#os.rmdir('/home/zac/Documents/Test_Dup')

shutil.rmtree('/home/zac/Documents/Test_Dup')
