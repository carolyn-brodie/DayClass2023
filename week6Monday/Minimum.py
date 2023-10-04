##The Minimum

##Set minimumSoFar = first thing.
##Check each thing in turn:
##		If thing is SMALLER than minimumSoFar
##			(in the appropriate sense)
##		 minimumSoFar = thing
##Return minimumSoFar.


def findMinimum(lst):
    """retrun the smallest item in lst
    :param lst: list of numbers
    :return: integer
    >>> findMinimum([100,10, 34])
    10
    >>> findMinimum([34])
    0
        """
    minimumSoFar = lst[0]
    for element in lst:
        if element < minimumSoFar:
            minimumSoFar = element
    return minimumSoFar


##test
# theList = [10,2,-5, 14, 6]
# print(findMinimum(theList))
