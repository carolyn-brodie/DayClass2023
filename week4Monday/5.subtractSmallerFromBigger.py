##Write a program that inputs 2 integers, repeatedly subtracts the
##smaller from the larger until the result is smaller than the smaller one,
##and displays the number of subtractions.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
count = 0


if number1 < number2:
    temp  = number1
    number1 = number2
    number2 = temp
 
result = number1
while result >= number2:
    result -= number2
    count += 1


 
print(count)
    

