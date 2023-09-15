#Write a program to compute the average of numbers entered by the user.
#The number of numbers is not known ahead of time.


#option 1
total = 0
count = 0
done = False
while not done:
    numberStr = input("Enter a number (enter to end): ")
    if numberStr == "":
        done = True
    else:
        number = float(numberStr)
        total += number
        count += 1
print("The average is", total/count)
