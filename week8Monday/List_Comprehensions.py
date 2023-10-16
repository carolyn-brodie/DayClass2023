def squareIt(number):
    return number ** 2

def isGreater20(number):
    return number > 20

list_of_numbers = [1, 4, 5, 6, 10]

total = sum([squareIt(x) for x in list_of_numbers if isGreater20(squareIt(x))])
print(total)

## First Sum
## built in function to add all the numbers in a list
print(sum([1, 2, 3]))

#Square all the numbers in a list
numbers_squared = [squareIt(x) for x in list_of_numbers]
print(numbers_squared)

# print([x ** 2 for x in list_of_numbers])

## filter
filtered = [num for num in numbers_squared if isGreater20(num)]
print(filtered)

numbers_squared = [squareIt(x) for x in list_of_numbers]
filtered = [num for num in numbers_squared if isGreater20(num)]
total = sum(filtered)
print("total is ", total)
