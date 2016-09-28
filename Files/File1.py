"""
This program shows how os.path.join() joins the path for files
"""

import os
print(os.path.join('usr','bin','path'))


myfiles = ['accounts.txt','details.csv','invite.docx']
for filename in myfiles:
    print(os.path.join('/usr/rahul/home',filename))
