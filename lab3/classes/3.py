class Shape():
    def __init__(self):
        self.area = 0
'''
    def printarea(self):
        print(self.area)
'''

class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length
    def area(self):
        print(self.length * self.width)

x = Rectangle(int(input()), int(input()))
x.area()
 # x.printarea()
