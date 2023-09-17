##Write a program that inputs 2 integers, repeatedly subtracts the
##smaller from the larger until the result is smaller than the smaller one,
##and displays the number of subtractions.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
count = 0

multipler = 1

if number2 < 0 and number1 >= 0:
    multipler = -1

elif number1 < 0 and number2 >= 0:
    multipler = -1

number1 = abs(number1)
number2 = abs(number2)

if number1 < number2:
    temp  = number1
    number1 = number2
    number2 = temp


result = number1
if number2 == 0:
    result = -1

print(result, number2)
while result >= number2:
    result -= number2
    count += 1
print(count * multipler)
    

