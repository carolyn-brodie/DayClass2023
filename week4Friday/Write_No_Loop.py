outputList = ["Line 0", "Line 1", "Line 2", "Line 3"]

# ## Add new line characters
# modified_output = []
# for item in outputList:
#     modified_output.append(item + "\n")


file = open("./myData/out.txt","w")
# file.writelines(outputList)
file.writelines(modified_output)
file.close()