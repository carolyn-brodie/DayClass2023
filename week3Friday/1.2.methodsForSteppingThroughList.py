myList = [10,20,30,40]

print(myList)
## First way to move through a list
for element in myList:
    print("element is", element)








##Second way to move through a list
for index in range(4):
    print("index is", index, "element is", myList[index])


## change the code above so that it works if the list has more or less
## than 4 items
