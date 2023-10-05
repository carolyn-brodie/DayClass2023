

def mystery(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_minus_1 = 1
        n_minus_2 = 0
        for i in range(2, n + 1):
            new_n = n_minus_1 + n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = new_n
        return new_n


def tester():
    print(mystery(6))

tester()