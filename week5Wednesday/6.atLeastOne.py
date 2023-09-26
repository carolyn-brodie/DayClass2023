##At Least One

##Check each thing in turn:
##		If thing HAS the property:
##			Return True.
##Return False.

def findAtLeastOne(lst, value):
    found = False
    count = 0
    while (not found) and count < len(lst):
        if lst[count] == value:
            found = True
        count += 1
    return found


##test
theLst = [5, 10, 20, -5]
print(findAtLeastOne(theLst, 15))
