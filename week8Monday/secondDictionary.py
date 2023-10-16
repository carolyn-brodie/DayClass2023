test = {"A" : 1, "B" : 2}
print(test["B"])

##I can change individual values and use them for other purposes
test["A"] += 1
print(test["A"])

##I can add new pairs to the dictionary
test["C"] = 3

##Print the whole dictionary
print(test)

##If you try to access  a key that is not in the dictionary you get an error
##print(test["D"])

##Instead test before you use it
if "D" in test:
    print(test["D"])
else:
    print("not in dictionary")


##Iterating over the dictionary
print("Iterating over the list and printing on one line")
for key in test:
	print(key, end = " ")
print()

##Iterating and printing out key -> value pairs
for key, value in test.items():
	print(key, "->", value)


##Making an accumulator
total = 0
for value in test.values():
	total += value
print("total is", total)


