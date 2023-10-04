#import doctest

## The all algorithm

##Start with the assumption that everything has the property
##Check each thing in turn:
##		If thing does NOT have the property:
##			Return False.
##Return True.
##Check if everything in the list is greater than value
def findAllTrue(lst, value):
    """
    Return True if everything in lst is greater than value
    :param lst: list of numbers
    :param value: integer
    :return: boolean
    >>> findAllTrue([16,20], 15)
    True
    >>> findAllTrue([], 15)
    True
    >>> findAllTrue([10, 20], 25)
    False
    """
    for item in lst:
        if item <= value:
            return False
    return True


# if __name__ == '__main__':
#     doctest.testmod(verbose=True)
##Test

# theList = [10 , -2, 4, 1, 5]
# print(findAllTrue(theList, 0))
