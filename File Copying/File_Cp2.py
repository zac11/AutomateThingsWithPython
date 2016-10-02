import send2trash,os
baconfile = open('/home/zac/Documents/bacon.txt','w')
baconfile.write('bacon is not a vegetable')
baconfile.close()
send2trash.send2trash('/home/zac/Documents/bacon.txt')
