##Function to create a birthday greeting

def modifiedCreateGreeting(name):
    out = "Happy birthday to you!  Happy birthday to you!  Happy birthday dear " + name +".\n"
    ##print(out)
    return out



def singBirthdaySong(name):
    mainStr = modifiedCreateGreeting(name)
    print(mainStr + "Happy Birthday to You")


##Main Program
modifiedCreateGreeting("Sam")
#print(modifiedCreateGreeting("Sam"))
#singBirthdaySong("Sam")
