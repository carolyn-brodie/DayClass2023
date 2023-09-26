##Which (return the list of things that are greater than a value

##Set outputList = empty
##Check each thing in turn:
##		If thing HAS the property:
##			add thing to outputList
##Return outputList.


def whichItems(lst, value):
    outList = []
    for item in lst:
        if item > value:
            outList.append(item)
    return outList


##Testing
theLst = [10, 2, -5,6]

print(whichItems(theLst, 5))
