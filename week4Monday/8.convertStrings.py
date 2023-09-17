#Write a program to convert a list of numerals to a list of integers

myList = ['2','56','5','29','-1']
newList = []

for item in myList:
    newList.append(int(item))

print(myList)
print(newList)
