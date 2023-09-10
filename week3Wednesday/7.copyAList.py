test = [1, 5, -3, 0, 66]
testCopy = list(range(len(test)))
print("first:", testCopy)
for index in range(len(test)):
    testCopy[index] = test[index]

print(testCopy)
print(test)
