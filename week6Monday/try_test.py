


# define a function to test
def factorial(n):
    '''
    This function calculates recursively and
    returns the factorial of a positive number.
    Define input and expected output:
    :param n: int # a positive integer
    :return: int
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    '''
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# call the testmod function
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
