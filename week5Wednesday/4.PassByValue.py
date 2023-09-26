#Pass by value for scalars

def testPassByValue(number):
    number += 10
    print("Inside function num is", number) 



##Main Program
num = 5
print("Before call, num is", num)
testPassByValue(num)
print("After call, num is", num)
    
