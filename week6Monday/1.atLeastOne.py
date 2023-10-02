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
    """
    def findAtLeastOne(lst, value):
        """
        Return True if at least one item in lst is greater than value
        :param lst: list of numbers
        :param value:   integer
        :return:    boolean
        """

    for item in lst:
        if item > value:
            return True
    return False


##test
theLst = [5, 10, 20, -5]
print(findAtLeastOne(theLst, 15))
