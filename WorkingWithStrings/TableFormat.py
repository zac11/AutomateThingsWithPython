"""
This program takes a dictionary of items and uses the center() and the ljust(),rjust() method to print the
contents of the dictionary in a nice tabular format

"""


def printTableFormat(itemsDict,leftWidth,rightWidth):
    print('Items in Table Format'.center(leftWidth+rightWidth,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,".") + str(v).rjust(rightWidth))

picnicItems={'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printTableFormat(picnicItems, 12, 5)
printTableFormat(picnicItems, 20, 6)