## rectangle

class Rectangle (object):


    def __init__(self, length, width):
        self.length = length
        self.width = width


##    def returnWidth(self):
##        return self.width

    def calculateArea(self):
        return self.length * self.width


    def __str__(self):
        return "Rectangle with " + str(self.length) + " x " + str(self.width)


##Test
def test():
    rect1 = Rectangle(3,2)
    print(rect1)
    print("area of rectangle is" , rect1.calculateArea())

if __name__ == "__main__":
    test()


