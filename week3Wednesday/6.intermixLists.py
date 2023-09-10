##intermix two lists

list1 = [0,1,2,3,4]
list2 = [9,8,7,6,5]

mixedList = []
for count in range(len(list1)):
    mixedList.append(list1[count])
    mixedList.append(list2[count])

print(mixedList)

##What happens if the lists are not the same length?  Let's fix it so it works then

 
