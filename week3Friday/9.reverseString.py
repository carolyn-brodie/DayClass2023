##Write a program to reverse a string using a loop 

myStr = "This is a Test"
newStr = ""

for index in range(len(myStr)-1,-1,-1):
    newStr = newStr + myStr[index]

print(newStr)
    


## In Python the easy way is as follows:

newStr = myStr[len(myStr)-1:: -1]
print(newStr)
