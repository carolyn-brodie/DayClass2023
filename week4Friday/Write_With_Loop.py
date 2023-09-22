
outputList = ["Line 0", "Line 1", "Line 2", "Line 3"]

file = open("./myData/out.txt", "w")
for item in outputList:
    file.write(item + "\n")
file.close()

