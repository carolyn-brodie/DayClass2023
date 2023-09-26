

def changeList(theList):
    if len(theList) > 0:
        theList[0] = "New Value"
    print("done")


lst = [1, 2, 3]
print(lst)
changeList(lst)
print(lst)
