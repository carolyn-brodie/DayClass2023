

def mystery(n):
    '''
    function returns the nth number in the fibonacci sequence
    :param n: int
    :return: int - the nth number in the fibonacci sequence
    >>> mystery(0)
    0
    >>> mystery(1)
    1
    >>> mystery(2)
    1
    >>> mystery(3)
    2
    >>> mystery(6)
    8
    '''
    if n == 0:                      # Test to see if input is 0, if so return 0
        return 0
    elif n == 1:                    # Test to see if input is 1, if so return 1
        return 1
    else:                           # In all other cases do the following
        n_minus_1 = 1               # set n_minus_1 to 1
        n_minus_2 = 0               #
        for i in range(2, n + 1):
            new_n = n_minus_1 + n_minus_2 # add n_minus_1 and n_minus_2
            n_minus_2 = n_minus_1         # set n_minus_2 to n_minus_1
            n_minus_1 = new_n             # set n_minus_1 to new_n
        return new_n                # return new_n at end of loop


def tester():
    print(mystery(6))


# if __name__ == '__main__':
#
#     tester()