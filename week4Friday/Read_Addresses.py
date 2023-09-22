# Method 1
# filename = "./myData/addresses.txt"
# file = open(filename,"r")
# data = file.read().split("\n")
# file.close()
#
# output = ""
# for address in data:
#     output += address + "; "
# print(output)

# filename = "./myData/addresses.txt"
# file = open(filename,"r")
# data = file.readlines()
# file.close()
# print(data)
#
# output = ""
# for address in data:
#     address = address.strip()
#     output += (address + ";")
# print(output)