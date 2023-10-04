##At Least One

##Check each thing in turn:
##		If thing HAS the property:
##			Return True.
##Return False.

def findAtLeastOne(lst, value):
    """
    Return True if at least one item in lst is greater than value
    :param lst: list of numbers
    :param value:   integer
    :return:    boolean
    >>> findAtLeastOne([10,20], 15)
    True
    >>> findAtLeastOne([], 15)
    False
    >>> findAtLeastOne([10, 20], 25)
    False
    """

    for item in lst:
        if item > value:
            return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
##test
# theLst = [5, 10, 20, -5]
# print(findAtLeastOne(theLst, 15))
