import functools
import operator

##Nonfunctional style
def square_list(lst):
    out_list = []
    for number in lst:
        out_list.append(number ** 2)
    return out_list


list_of_numbers = [1, 4, 5, 6, 10]
print(square_list(list_of_numbers))


## Removing small squares
def square_list(lst):
    out_list = []
    for number in lst:
        square = number ** 2
        if square > 20:
            out_list.append(square)
    return out_list

##Functional style
def squareIt(number):
    return number ** 2

def isGreater20(number):
    return number > 20


## Map example
squared = list(map(squareIt, list_of_numbers))

print("Result of mapping", squared)

## Filter Example
filtered = list(filter(isGreater20, squared))
print("Result of filtering", filtered)

## Reduce Example
summed = functools.reduce(operator.add, filtered)
print("Result of reducing", summed)


