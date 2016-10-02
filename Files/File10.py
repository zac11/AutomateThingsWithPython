import shelve
shelfFile=shelve.open('mydata.txt')
cats=['olivia','meredith','nala','white cofee cat']
shelfFile['cats']=cats
shelfFile.close()

