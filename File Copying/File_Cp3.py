import os
"""
Walking through the directory and listing out all its sub directories and folder names

"""

for folderName,subFolderName,fileName in os.walk('/home/zac/Downloads'):
    print('The current folder name is '+folderName)

    for subFolder in subFolderName:
        print('Subfolder of '+folderName + ' is : '+subFolder)

        for files in fileName:
           print('File inside '+folderName+'is :'+files)

print('')