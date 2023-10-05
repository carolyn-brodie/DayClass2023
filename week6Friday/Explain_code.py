
def square_elements(lst):
    """
    Square all the elements of a list
    :param lst: list of numbers
    :return: list of numbers squared
    """
    return [e ** 2 for e in lst]


print(square_elements([4, 6, 8]))