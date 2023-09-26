## The all algorithm

##Start with the assumption that everything has the property
##Check each thing in turn:
##		If thing does NOT have the property:
##			Return False.
##Return True.
##Check if everything in the list is greater than zero
def findAllTrue(lst, value):
    found = True
    count = 0
    while found and (count < len(lst)):
         
        if lst[count] <= value:
            found = False
        count += 1
    return found

##Test

theList = [10 , 2, 4, 1, -5]
print(findAllTrue(theList, 0))
