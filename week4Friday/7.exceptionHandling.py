## Try except

done = False
while not done:
    numStr =input("Enter a non-zero integer, press enter to quit: ")
    if numStr == '':
        done = True
    else:
        number = int(numStr)
        x = 5/number
        print(x)
       
        
