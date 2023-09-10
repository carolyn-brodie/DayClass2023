myList = ["apples", "oranges", 2]
print(myList)

print(myList[1])

if myList[0] == "apples":
    print("It is apples")

newList = [myList[2], myList]
print (newList)
## Break string apart
print(list("hi there"))

##join list
lst1 = ["a","b","c"]
separator = ""
out = separator.join(lst1)
print(out)