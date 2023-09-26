##Example of an accumulator function

##Sum all the numbers between zero and number

def sumNumbers(number):
    total = 0
    for value in range(number+1):
        total += value
    return total


print(sumNumbers(5))


##Make a sentence out of user words
def makeSentence():
    outString = ""
    done = False
    while not done:
        word = input("Enter a word, q to quit: ")
        if word == "q":
            done = True
        else:
            outString = outString + word + " "
    return outString

print(makeSentence())