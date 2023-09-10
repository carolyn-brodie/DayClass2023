## Find all the vowels in this string

userInput = input("Type something: ")
for letter in userInput:
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print(letter, end=" ")

