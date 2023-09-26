## How many greater than a value

##Set counter = 0.
##Check each thing in turn:
##		If thing HAS the property:
##			increase counter by 1.
##Return counter.


def findHowMany(lst, value):
    counter = 0
    for item in lst:
        if item > value:
            counter += 1
    return counter


##Testin
theList = [10, 2, -1, 6]
print(findHowMany(theList, 5))
