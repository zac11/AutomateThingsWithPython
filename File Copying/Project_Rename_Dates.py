#!python3
#Renames files with american date format MM-DD-YYYY to be in the European DD-MM-YYYY format

import shutil,os,re

#Create a regex pattern to recognize the date with american format

datepattern=re.compile(r"""^(.*?)  #text before date
(0|1)?\d-                          #one or two digits for month
((0|1|2|3)?\d)-                    #one or two digits for the day
((19|20)\d\d)                      #four digits for the year
(.*?)$""",re.VERBOSE)              #text after the date

#Todo : Loop over file in working directory
for americanFiles in os.listdir('.'):

    mo=datepattern.search(americanFiles)
# Todo : Skip files without date
    if mo==None:
        continue

#Todo : Get different parts of file
    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4)
    yearpart = mo.group(6)
    afterpart = mo.group(8)



#Todo : Form European style date
    europeandate = beforepart + daypart+'-'+monthpart+'-'+yearpart+afterpart

#Todo : Get full, absolute file path
    absWorkDir = os.path.abspath('.')
    americanFiles = os.path.join(absWorkDir,americanFiles)
    europeandate = os.path.join(absWorkDir,europeandate)

#Todo : Rename the files
    print('Renaming "%s" to "%s"...'%(americanFiles,europeandate))




