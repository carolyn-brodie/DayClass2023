# def mystery(firstNumber, secondNumber):
#     if firstNumber <= secondNumber:
#         print(firstNumber, end=" ")
#         mystery(firstNumber +1 , secondNumber)
#
#
# mystery(2, 5)

# def mystery1(x, y):
#     if (y == 0):
#         return 1;
#     elif (y < 0):
#         return 1 / mystery1(x,-y)
#     else:
#         return x * mystery1(x, y-1)
#
# print(mystery1(3,-2))

# def divideRepeatedly(x):
#     if x < 2:
#         return 0
#     else:
#         return 1 + divideRepeatedly(x/2)
#
# print(divideRepeatedly(12))
#
# def mystery5(theString):
#     if len(theString) == 0:
#         return []
#     else:
#         return [theString[0]] + mystery5(theString[1:])
#
# print(mystery5("Hi t"))



