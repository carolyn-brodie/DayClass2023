## Sample For loop using a list

lst = [1,5,7,8]

for item in lst:
    print(item)

total = 0
for item in lst:
    print(f"total {total + item} = {total} + {item}")
    total += item
print(f"Sum of all items in the list = {total}")

