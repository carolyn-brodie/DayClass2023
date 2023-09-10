import math

#print(math.pi * 49 * 1/8)

radius = input("Enter the radius of the pizza: ")
radius = int(radius)
number_of_slices = int(input("Enter the number of slices: "))
print((math.pi * radius ** 2) / number_of_slices)