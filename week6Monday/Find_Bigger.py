

def larger(num1, num2):                          #Signature
    """                                         #Docstring
    num1 and num2 are two numbers.
    Return the larger of the two numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    print(larger(3,2), 2)
    print(larger(0,5), 5)
    print(larger(3,3), 3)

if __name__ == "__main__":
    main()



